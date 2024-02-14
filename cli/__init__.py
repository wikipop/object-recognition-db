class ChooseOption:
    def __init__(self, options_list: {any: any}):
        self.options = options_list

    def __call__(self, start_text="Choose an option: ", wrong_text="Invalid option. Please try again."):
        print(start_text)
        print(" ")

        for k, v in self.options.items():
            print(f"* {k}. {v}")

        print(" ")
        choice = int(input("Enter option number: "))

        if choice not in self.options:
            print(wrong_text)
            return self.__call__(start_text)

        return self.options[choice]


class EnumeratedChooseOption(ChooseOption):
    def __init__(self, options_list: [any]):
        super().__init__({i: option for i, option in enumerate(options_list)})


class ListElements:
    def __init__(self, elements: [any]):
        self.elements = elements

    def __call__(self):
        for element in self.elements:
            print(f"- {element}")