from logging.config import fileConfig
from alembic import context

from models.models import Base
from db.database import engine

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    """Run migrations in 'online' mode asynchronously."""
    connectable = engine

    await context.run_async(
        connectable,
        lambda connection: connection.run_sync(do_run_migrations)
    )


def do_run_migrations(connection):
    """Функция для выполнения миграций с синхронным соединением."""
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
    )


if __name__ == "__main__":
    if context.is_offline_mode():
        run_migrations_offline()
    else:
        import asyncio
        asyncio.run(run_migrations_online())
