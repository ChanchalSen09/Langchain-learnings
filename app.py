from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama


def main() -> None:
    llm = ChatOllama(
        model="llama3.2:3b",
        base_url="http://localhost:11434",
        temperature=0.7,
    )

    prompt = ChatPromptTemplate.from_template(
        "Explain the following topic in simple words for a beginner: {topic}"
    )

    chain = prompt | llm

    while True:
        topic = input("Enter a topic (or 'exit'): ").strip()
        if topic.lower() in {"exit", "quit"}:
            print("Bye!")
            break
        if not topic:
            print("Please enter a topic.")
            continue

        response = chain.invoke({"topic": topic})
        print("\nAnswer:\n")
        print(response.content)
        print()


if __name__ == "__main__":
    main()
