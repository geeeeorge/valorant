from .adapter.controllers.healthz import HealthzController
from .adapter.controllers.line_api_controller import LineApiController
from .application.line_api_usecase import LineApiUsecase
from .infrastructure.db_drivers.engine import get_engine
from .infrastructure.servers.route import get_route


def main():
    # dotenv.load_dotenv()  # .envファイルに以下の5つを用意する必要がある
    # engine = get_engine(
    #    os.environ.get("DATABASE"),
    #    os.environ.get("DB_USERNAME"),
    #    os.environ.get("DB_PASSWORD"),
    #    os.environ.get("DB_HOST"),
    #    os.environ.get("DB_PORT"),
    # )
    route = get_route(
        healthz_controller=HealthzController(),
        line_api_controller=LineApiController(LineApiUsecase()),
    )
    return route
