from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy


class SQLAlchemy(_SQLAlchemy):

    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e


db = SQLAlchemy()


