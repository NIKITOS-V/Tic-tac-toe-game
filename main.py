from Model.Service import Service
from Presenter.Presenter import Presenter
from View.TicTacToe import TicTacToeApp

if __name__ == "__main__":
    service = Service()

    presenter = Presenter(service)

    view = TicTacToeApp(presenter)

    view.run()
