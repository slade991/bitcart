"""Add shipping address

Revision ID: d42daa00adf8
Revises: 73d794ea10e2
Create Date: 2022-02-25 21:19:52.102928

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "d42daa00adf8"
down_revision = "73d794ea10e2"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("invoices", sa.Column("shipping_address", sa.Text(), nullable=True))
    op.add_column("invoices", sa.Column("notes", sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("invoices", "notes")
    op.drop_column("invoices", "shipping_address")
    # ### end Alembic commands ###
