"""inventory history model

Revision ID: 4dc459b038bd
Revises: dd6d0885882f
Create Date: 2023-10-03 03:48:39.519600

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4dc459b038bd'
down_revision: Union[str, None] = 'dd6d0885882f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('inventory_history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('quantity_change', sa.Integer(), nullable=True),
    sa.Column('new_quantity', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_inventory_history_id'), 'inventory_history', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_inventory_history_id'), table_name='inventory_history')
    op.drop_table('inventory_history')
    # ### end Alembic commands ###
