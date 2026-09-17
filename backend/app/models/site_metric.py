import uuid
from datetime import date

from sqlalchemy import Date, ForeignKey, Numeric
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.site import Site


class SiteMetric(Base):
    __tablename__ = "site_metrics"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    site_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("sites.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    recorded_at: Mapped[date] = mapped_column(
        Date,
        nullable=False,
        index=True,
    )

    carbon_sequestered: Mapped[float | None] = mapped_column(
        Numeric(12, 2),
        nullable=True,
    )

    biodiversity_score: Mapped[float | None] = mapped_column(
        Numeric(5, 2),
        nullable=True,
    )

    tree_cover: Mapped[float | None] = mapped_column(
        Numeric(5, 2),
        nullable=True,
    )

    site: Mapped["Site"] = relationship()
