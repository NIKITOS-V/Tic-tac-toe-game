from View.Formating.Errors import ColorError


class ParseColor:
    __min_shade_value = 0
    __max_shade_value = 255

    __min_alfa_value = 0.
    __max_alfa_value = 1.

    def __is_correct_values(self, red: int, green: int, blue: int, alfa: float) -> bool:
        """
        Функция проверки введённых оттенков на корректность.

        :param red: *int* ∈ [0, 255]
        :param green: *int* ∈ [0, 255]
        :param blue: *int* ∈ [0, 255]
        :param alfa: *float* ∈ [0, 1]

        :return: *bool*
        """

        return (
                self.__min_shade_value <= red <= self.__max_shade_value and
                self.__min_shade_value <= green <= self.__max_shade_value and
                self.__min_shade_value <= blue <= self.__max_shade_value and
                self.__min_alfa_value <= alfa <= self.__max_alfa_value
        )

    def get_color(self, red: int, green: int, blue: int, alfa: float = 1.) -> list[float]:
        """
        Функция перевода цвета rgb формата в процентный вид.

        :param red: *int* ∈ [0, 255]
        :param green: *int* ∈ [0, 255]
        :param blue: *int* ∈ [0, 255]
        :param alfa: *float* ∈ [0, 1]
        :return: [**red** / 255, **green** / 255, **blue** / 255]
        """

        if self.__is_correct_values(red, blue, green, alfa):
            return [
                float(red / self.__max_shade_value),
                float(green / self.__max_shade_value),
                float(blue / self.__max_shade_value),
                float(alfa)
            ]

        else:
            raise ColorError()
