import ruly

knowledge_base = ruly.knowledge_base.create([
    "IF color = 'red' THEN creature = 'dragon'",
    "IF color = 'grey' THEN creature = 'rat'"
])

print(ruly.backward_chain(knowledge_base, 'creature', color='red'))