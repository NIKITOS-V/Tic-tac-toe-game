from accessify import private

from View.Formating.Errors import ColorError


class ParseColor:
    __minColorValue = 0
    __maxColorValue = 255

    @private
    def is_correct_values(self, red: int, green: int, blue: int) -> bool:
        return (
                self.__minColorValue <= red <= self.__maxColorValue and
                self.__minColorValue <= green <= self.__maxColorValue and
                self.__minColorValue <= blue <= self.__maxColorValue
        )

    def get_color(self, red: int, green: int, blue: int) -> tuple:
        """
        :param red: *int* ∈ [0, 255]
        :param green: *int* ∈ [0, 255]
        :param blue: *int* ∈ [0, 255]
        :return: (**red** / 255, **green** / 255, **blue** / 255)

        Функция перевода цвета rgb формата в процентный вид.
        """
        if self.is_correct_values(red, blue, green):
            return red / self.__maxColorValue, green / self.__maxColorValue, blue / self.__maxColorValue

        else:
            raise ColorError()
