"""empty message

Revision ID: 09f38fe306a4
Revises: 155dcbad36df
Create Date: 2023-03-08 11:57:23.566779

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "09f38fe306a4"
down_revision = "155dcbad36df"
branch_labels = None
depends_on = None


def upgrade():  # noqa
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("forecast_value", sa.Column("adjust_mw", sa.Float(), nullable=True))
    op.add_column(
        "forecast_value_last_seven_days", sa.Column("adjust_mw", sa.Float(), nullable=True)
    )
    op.add_column("forecast_value_latest", sa.Column("adjust_mw", sa.Float(), nullable=True))
    op.add_column("forecast_value_old", sa.Column("adjust_mw", sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():  # noqa
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("forecast_value_old", "adjust_mw")
    op.drop_column("forecast_value_latest", "adjust_mw")
    op.drop_column("forecast_value_last_seven_days", "adjust_mw")
    op.drop_column("forecast_value", "adjust_mw")
    # ### end Alembic commands ###