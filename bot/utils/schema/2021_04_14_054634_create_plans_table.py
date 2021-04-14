from orator.migrations import Migration


class CreatePlansTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('plans') as table:
            table.increments('id')
            table.integer('provider_id').unsigned()
            table.foreign('provider_id').references('id').on('providers').on_delete('cascade')
            table.text('name')
            table.text('description')
            table.float('price')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('plans')
