from server import server, db
from server.models import User


@server.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User}
