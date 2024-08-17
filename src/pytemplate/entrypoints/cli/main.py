from src.pytemplate.domain.models import operands_factory
from src.pytemplate.service.calculator import Calculator


def main():
    first_operand = int(input("Enter the first operand: "))
    second_operand = int(input("Enter the second operand: "))
    action = input("Enter the action (e.g., add, subtract, multiply, divide): ")

    calculator = Calculator()

    if action == "add":
        result = calculator.add(operands_factory(first_operand, second_operand))
    elif action == "subtract":
        result = calculator.subtract(operands_factory(first_operand, second_operand))
    elif action == "multiply":
        result = calculator.multiply(operands_factory(first_operand, second_operand))
    elif action == "divide":
        result = calculator.divide(operands_factory(first_operand, second_operand))
    else:
        raise ValueError("Invalid action")

    return result


if __name__ == "__main__":
    main()
