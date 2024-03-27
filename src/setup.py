from setuptools import setup


def main():
    setup(
        name='flake8-one-letter-variables',
        version='0.0.1',
        zip_safe=False,
        py_modules=['flake8_one_letter_variables'],
        install_requires=[
            'flake8',
        ],
        entry_points={
            'flake8.extension': [
                'OLV001 = flake8_one_letter_variables:OneLetterVariableChecker',
            ],
        },
    )


if __name__ == '__main__':
    main()
