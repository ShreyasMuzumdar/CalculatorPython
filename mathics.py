import argparse
from mathics import mathics

def evaluate_expression(expression):
    """Evaluate the provided mathematical expression using Mathics."""
    mathics_session = Mathics()  # Start a Mathics session
    result = mathics_session.evaluate(expression)
    mathics_session.close()  # Close the session after evaluation
    return result

def main():
    # Set up the argument parser
    parser = argparse.ArgumentParser(description="Evaluate a mathematical expression using Mathics.")
    
    # Add argument for the mathematical expression
    parser.add_argument('expression', type=str, help='The mathematical expression to evaluate.')
    
    # Parse the command-line arguments
    args = parser.parse_args()

    # Evaluate the expression using Mathics
    result = evaluate_expression(args.expression)

    # Print the result
    print(f'Result: {result}')

if __name__ == "__main__":
    main()
