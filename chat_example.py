from langchain_ollama import ChatOllama


def main() -> None:
    llm = ChatOllama(
        model="llama3.2:3b",
        base_url="http://localhost:11434",
        temperature=0.7,
    )

    while True:
        message = input("You: ").strip()
        if message.lower() in {"exit", "quit"}:
            print("Assistant: Bye!")
            break
        if not message:
            continue

        response = llm.invoke(message)
        print(f"Assistant: {response.content}\n")


if __name__ == "__main__":
    main()
