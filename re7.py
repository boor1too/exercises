def snake_to_camel_case(snake_str):
    components = snake_str.split('_')
    # capitalize the first letter of each split word except the first one
    return components[0] + ''.join(x.title() for x in components[1:])

snake_str = "my_snake_case_string"
camel_str = snake_to_camel_case(snake_str)

print(camel_str)