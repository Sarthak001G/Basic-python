"""Use of match
When to Use match?
Handling commands or enums.
Matching data structures like tuples, dictionaries, or lists.
Simplifying long if-elif chains.
When deconstructing and analyzing nested structures.
Why Use match?
Readable Alternative to if-elif Chains:

Cleaner and more intuitive for scenarios with multiple conditions.
Powerful Pattern Matching:

Can match against complex data structures and decompose them.
Default Case:

The _ case ensures that unmatched cases are handled, similar to a default clause in switch.
Key Features:
Patterns:

You can match exact values, data structures, or even use variable bindings.
Wildcards (_):

A placeholder that matches anything (like a default case).
Guards (if conditions):

Add conditions to make the matching more specific.
Deconstruction:

You can unpack data structures like tuples or dictionaries in a pattern.32
SYNTAX"""
command = "start"

match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case "pause":
        print("Pausing...")
    case _:
        print("Unknown command.")


"""use of point"""
point = (3, 5)

match point:
    case (0, 0):
        print("Origin")
    case (x, 0):
        print(f"Point on the X-axis at {x}")
    case (0, y):
        print(f"Point on the Y-axis at {y}")
    case (x, y):
        print(f"Point at ({x}, {y})")


"Example =3"
number = 42

match number:
    case n if n % 2 == 0:
        print(f"{n} is an even number")
    case _:
        print(f"{number} is an odd number")


"Example = 4"
data = {"action": "move", "value": 10}

match data:
    case {"action": "move", "value": v}:
        print(f"Moving by {v} units")
    case {"action": "stop"}:
        print("Stopping")
    case _:
        print("Unknown action")
