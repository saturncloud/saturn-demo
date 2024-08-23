import time

import click


@click.command
@click.argument('x')
@click.argument('y')
def run(x, y):
    print('args', x, y)
    print('sleeping')
    time.sleep(10)
    if x == y:
        raise ValueError('x==y')
    print('exponent', x, y)
    print('RESULT:', float(x) ** float(y))
    
    
if __name__ == "__main__":
    run()