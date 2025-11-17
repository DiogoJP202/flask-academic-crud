import pytest
from datetime import date

from app import app
from model.database import db
from model.professor import Professor
from model.turma import Turma
from model.aluno import Aluno
from controller.turma_controller import TurmaController


@pytest.fixture()
def app_ctx():
    app.config.update(
        TESTING=True,
        SQLALCHEMY_DATABASE_URI="sqlite:///:memory:",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture()
def client(app_ctx):
    return app_ctx.test_client()


def test_criar_aluno_persiste_campos_convertidos(client, app_ctx):
    with app_ctx.app_context():
        prof = Professor(nome="Prof", idade=40, materia="Mat", observacoes=None)
        db.session.add(prof)
        db.session.flush()
        turma = Turma(descricao="1A", ativo=True, professor_id=prof.id)
        db.session.add(turma)
        db.session.commit()
        turma_id = turma.id

    resp = client.post(
        "/alunos/criar_aluno",
        data={
            "nome": "Aluno X",
            "idade": "18",
            "turma": str(turma.id),
            "data_nasc": "2006-01-02",
            "nota_semestre_um": "7.5",
            "nota_semestre_dois": "8.0",
            "media_final": "7.75",
        },
        follow_redirects=False,
    )

    assert resp.status_code == 302
    with app_ctx.app_context():
        aluno = Aluno.query.filter_by(nome="Aluno X").first()
        assert aluno is not None
        assert aluno.idade == 18
        assert aluno.turma_id == turma.id
        assert aluno.data_nascimento == date(2006, 1, 2)
        assert aluno.nota_primeiro_semestre == 7.5
        assert aluno.media_final == 7.75


def test_criar_turma_sem_checkbox_fica_inativa(client, app_ctx):
    with app_ctx.app_context():
        prof = Professor(nome="Prof B", idade=35, materia="História", observacoes=None)
        db.session.add(prof)
        db.session.commit()
        prof_id = prof.id

    resp = client.post(
        "/turma/criar_turma",
        data={"descricao": "2B", "professor": str(prof_id)},
        follow_redirects=False,
    )

    assert resp.status_code == 302
    with app_ctx.app_context():
        turma = Turma.query.filter_by(descricao="2B").first()
        assert turma is not None
        assert turma.ativo is False


def test_turma_controller_delete_remove_sem_alunos(app_ctx):
    with app_ctx.app_context():
        prof = Professor(nome="Prof C", idade=45, materia="Geo", observacoes=None)
        db.session.add(prof)
        db.session.flush()
        turma = Turma(descricao="3C", ativo=True, professor_id=prof.id)
        db.session.add(turma)
        db.session.commit()
        turma_id = turma.id

        result = TurmaController.delete(turma_id)
        assert result is True
        assert Turma.query.get(turma_id) is None
