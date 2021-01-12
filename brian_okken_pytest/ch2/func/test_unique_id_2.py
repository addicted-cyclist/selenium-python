import pytest
import tasks
from tasks import Task


@pytest.mark.xfail(tasks.__version__ < '0.2.0',
                   reason='not supported until version 0.2.0')
def test_unique_id_3():
    """Вызов unique_id() дважды должен возвращать разные номера."""
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2

@pytest.mark.xfail()
def test_unique_id_is_a_duck():
    """Продемонстрирация xfail."""
    uid = tasks.unique_id()
    assert uid == 'a duck'


def test_unique_id_not_a_duck():
    """Продемонстрирация xpass."""
    uid = tasks.unique_id()
    assert uid != 'a duck'

@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """Connect to db before testing, disconnect after."""
    # Setup : start db
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    yield  # здесь происходит тестирование

    # Teardown : stop db
    tasks.stop_tasks_db()
