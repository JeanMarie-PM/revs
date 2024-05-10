from django.test import TestCase
from model_bakery import baker

from .models import Reporter

from django.db import connection


def dump_test_db_tables():
    """
    This function retrieves and prints the list of tables in the current test database.
    """
    cursor = connection.cursor()
    cursor.execute("SELECT table_name FROM information_schema.tables ;")
    tables = [row[0] for row in cursor.fetchall()]
    print("Tables in Test Database:")
    for table in tables:
        print(table)

    cursor.close()


class ReporterTest(TestCase):
    def setUp(self):
        for _ in range(6):
            baker.make(Reporter).save()

    def test_all_tables_exist(self):
        print("Tables in test db")
        dump_test_db_tables()

    def test_initial_state_has_log_entries(self):
        self.assertGreater(Reporter.objects.all().count(), 0)

    # def test_insert_should_be_tracked(self):
    #     pass

    # def test_update_name_should_not_be_tracked(self):
    #     pass

    # def test_update_email_should_be_tracked(self):
    #     pass

    # def test_delete_should_be_tracked(self):
    #     pass
