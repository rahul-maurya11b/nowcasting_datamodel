"""empty message

Revision ID: 46261a94d6a6
Revises: 14e1747b9710
Create Date: 2022-03-21 09:05:41.488024

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "46261a94d6a6"
down_revision = "14e1747b9710"
branch_labels = None
depends_on = None


def upgrade(): # noqa 103
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "gsp",
        sa.Column("created_utc", sa.DateTime(timezone=True), nullable=True),
        sa.Column("pk", sa.Integer(), nullable=False),
        sa.Column("label", sa.String(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=True),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("group", sa.String(), nullable=True),
        sa.Column("region_name", sa.String(), nullable=True),
        sa.Column("status_interval_minutes", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("pk"),
    )
    op.create_table(
        "gsp_yield",
        sa.Column("created_utc", sa.DateTime(timezone=True), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("datetime_utc", sa.DateTime(), nullable=True),
        sa.Column("solar_generation_kw", sa.String(), nullable=True),
        sa.Column("gsp_pk", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["gsp_pk"],
            ["gsp.pk"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_datetime_utc", "gsp_yield", [sa.text("datetime_utc DESC")], unique=False)
    op.create_index(op.f("ix_gsp_yield_datetime_utc"), "gsp_yield", ["datetime_utc"], unique=False)
    op.create_index(op.f("ix_gsp_yield_gsp_pk"), "gsp_yield", ["gsp_pk"], unique=False)
    op.drop_table("location")
    op.drop_constraint(None, "forecast", type_="foreignkey")
    op.create_foreign_key(None, "forecast", "gsp", ["location_id"], ["pk"])
    # ### end Alembic commands ###


def downgrade(): # noqa 103
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "forecast", type_="foreignkey")
    op.create_foreign_key(None, "forecast", "location", ["location_id"], ["id"])
    op.create_table(
        "location",
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.Column("label", sa.VARCHAR(), nullable=True),
        sa.Column("gsp_id", sa.INTEGER(), nullable=True),
        sa.Column("gsp_name", sa.VARCHAR(), nullable=True),
        sa.Column("gsp_group", sa.VARCHAR(), nullable=True),
        sa.Column("region_name", sa.VARCHAR(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.drop_index(op.f("ix_gsp_yield_gsp_pk"), table_name="gsp_yield")
    op.drop_index(op.f("ix_gsp_yield_datetime_utc"), table_name="gsp_yield")
    op.drop_index("ix_datetime_utc", table_name="gsp_yield")
    op.drop_table("gsp_yield")
    op.drop_table("gsp")
    # ### end Alembic commands ###
