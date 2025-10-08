class CalculatorConundrum {
    public String calculate(int operand1, int operand2, String operation) {
        if (operation == null) {
            throw new IllegalArgumentException("Operation cannot be null");
        } else if (operation == "") {
            throw new IllegalArgumentException("Operation cannot be empty");
        } else if (operation != "+" && operation != "-" && operation != "*" && operation != "/" ) {
            throw new IllegalOperationException("Operation '" + operation + "' does not exist" );
        }

        int result = 0;
        if (operation == "+") {
            result = operand1 + operand2;
        } else if (operation == "-") {
            result = operand1 - operand2;
        } else if (operation == "*") {
            result = operand1 * operand2;
        } else if (operation == "/") {
            try {
                result = operand1 / operand2;
            } catch (ArithmeticException e) {
                throw new IllegalOperationException("Division by zero is not allowed", e);
            }
        }
        
        return String.format("%d %s %d = %d", operand1, operation, operand2, result);
    }
}
