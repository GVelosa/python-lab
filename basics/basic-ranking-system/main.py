def main():
    grades: dict[str, float | int] = {
        "Spanish": 91.2,
        "Biology": 87,
        "History": 128.1,
        "Philosophy": 104.1,
        "Physics": 102.3,
        "Geography": 106.2,
        "English": 102.3,
        "Portuguese Literature": 101.4,
        "Math": 114,
        "Chemistry": 87.9,
        "Sociology": 113.1,
        "Writing Techniques": 99.9,
    }

    ranking = sorted(grades.items(), key=lambda item: item[1], reverse=True)

    for position, (name, score) in enumerate(ranking, start=1):
        print(f"{position}. {name} - {score}")


if __name__ == "__main__":
    main()