from orator.migrations import Migration


class CreateProvidersTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('providers') as table:
            table.increments('id')
            table.text('name')
            table.text('description')
            table.string('cover').nullable()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('providers')
