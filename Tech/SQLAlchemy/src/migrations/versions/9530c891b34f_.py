"""empty message

Revision ID: 9530c891b34f
Revises: 
Create Date: 2024-03-02 12:34:23.657683

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9530c891b34f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vacancies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('compensation', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('workers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('resumes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('compensation', sa.Integer(), nullable=True),
    sa.Column('workload', sa.Enum('part_time', 'full_time', name='workload'), nullable=False),
    sa.Column('worker_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', now())"), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', now())"), nullable=False),
    sa.CheckConstraint('compensation > 0', name='check_compensation_positive'),
    sa.ForeignKeyConstraint(['worker_id'], ['workers.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('title_index', 'resumes', ['title'], unique=False)
    op.create_table('vacancies_replies',
    sa.Column('resume_id', sa.Integer(), nullable=False),
    sa.Column('vacancy_id', sa.Integer(), nullable=False),
    sa.Column('cover_letter', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['resume_id'], ['resumes.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['vacancy_id'], ['vacancies.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('resume_id', 'vacancy_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vacancies_replies')
    op.drop_index('title_index', table_name='resumes')
    op.drop_table('resumes')
    op.drop_table('workers')
    op.drop_table('vacancies')
    # ### end Alembic commands ###
