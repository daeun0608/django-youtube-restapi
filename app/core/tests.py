from django.test import SimpleTestCase
from unittest.mock import patch
from django.core.management import call_command
from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg2OperationalError

# DB연결 시도를 가로채기
@patch('django.db.utils.ConnectionHandler.__getitem__')
class CommandsTests(SimpleTestCase):
    # 연결 성공
    def test_wait_for_db_ready(self, patched_getitem):
        patched_getitem.return_value = True

        call_command('wait_for_db')

        self.assertEqual(patched_getitem.call_count, 1)
    # 연결 오류
    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_getitem):
        patched_getitem.side_effect = [Psycopg2OperationalError] + \
            [OperationalError] * 5 + [True]

        call_command('wait_for_db')

        self.assertEqual(patched_getitem.call_count, 7)