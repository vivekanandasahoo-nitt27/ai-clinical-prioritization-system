from dotenv import load_dotenv
load_dotenv()

from who_rag import retrieve_who_context

def test_query(query):
    print("\n==============================")
    print(f"QUERY: {query}")
    print("==============================\n")
    
    result = retrieve_who_context(query)
    
    print(result)
    print("\n==============================\n")

if __name__ == "__main__":
    test_query("Severe chest pain and sweating")
    test_query("Unconscious patient not breathing")
    test_query("Heavy bleeding after accident")