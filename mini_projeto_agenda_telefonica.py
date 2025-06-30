contatos_salvos = []

while True:
    print("\n=== Sua Agenda Telefônica ===")
    print("1 - Adicionar Contato")
    print("2 - Mostrar Todos os Contatos")
    print("3 - Ver Detalhes de um Contato")
    print("4 - Modificar um Contato")
    print("5 - Apagar um Contato")
    print("6 - Sair do Programa")
    opcao = input("O que você quer fazer? ")

    if opcao == "1":
        if len(agenda) >= 5:
            print("Sua agenda tá cheia! Não dá pra adicionar mais contatos.")
        else:
            contato = {}

            while True:
                nome_contato = input("Primeiro nome (só letras, até 20 chars): ")
                if nome_contato.isalpha() and len(nome_contato) <= 20:
                    contato["nome_contato"] = nome_contato
                    break
                else:
                    print("Nome inválido, tente de novo.")

            while True:
                sobrenome_contato = input("Sobrenome (só letras, até 20 chars): ")
                if sobrenome_contato.isalpha() and len(sobrenome_contato) <= 20:
                    contato["sobrenome_contato"] = sobrenome_contato
                    break
                else:
                    print("Sobrenome inválido, tente de novo.")

            telefone_fixo = input("Telefone fixo (opcional, só números, até 15): ")
            if telefone_fixo != "" and (not telefone_fixo.isdigit() or len(telefone_fixo) > 15):
                print("Telefone fixo inválido, deixei em branco.")
                telefone_fixo = ""
            contato["telefone_fixo"] = telefone_fixo

            while True:
                telefone_celular = input("Celular (obrigatório, só números, até 15): ")
                if telefone_celular.isdigit() and len(telefone_celular) <= 15:
                    contato["telefone_celular"] = telefone_celular
                    break
                else:
                    print("Celular inválido, tente de novo.")

            while True:
                email_contato = input("Email (exemplo@dominio.com): ")
                if "@" in email_contato and "." in email_contato.split("@")[-1]:
                    contato["email_contato"] = email_contato
                    break
                else:
                    print("Email inválido, tente de novo.")

            while True:
                mes_nascimento = input("Mês de nascimento (1 a 12): ")
                if mes_nascimento.isdigit() and 1 <= int(mes_nascimento) <= 12:
                    contato["mes_nascimento"] = mes_nascimento
                    break
                else:
                    print("Mês inválido, tente outra vez.")

            while True:
                dia_nascimento = input("Dia de nascimento (1 a 31): ")
                if dia_nascimento.isdigit() and 1 <= int(dia_nascimento) <= 31:
                    contato["dia_nascimento"] = dia_nascimento
                    break
                else:
                    print("Dia inválido, tente de novo.")

            while True:
                ano_nascimento = input("Ano de nascimento (1900 a 2025): ")
                if ano_nascimento.isdigit() and 1900 <= int(ano_nascimento) <= 2025:
                    contato["ano_nascimento"] = ano_nascimento
                    break
                else:
                    print("Ano inválido, tente mais uma vez.")

            agenda.append(contato)
            print(f"Beleza! Contato {nome_contato} {sobrenome_contato} adicionado com sucesso.")

    elif opcao == "2":  
        if len(agenda) == 0:
            print("Sua agenda está vazia, bora adicionar contatos!")
        else:
            print("\nAqui estão seus contatos:")
            for i, c in enumerate(agenda, 1):
                print(f"{i} - {c['nome_contato']} {c['sobrenome_contato']}")

    elif opcao == "3":  
        nome_busca = input("Digite o primeiro nome do contato que quer ver: ")
        sobrenome_busca = input("Digite o sobrenome do contato: ")
        achou = False
        for c in agenda:
            if c["nome_contato"] == nome_busca and c["sobrenome_contato"] == sobrenome_busca:
                print("\nDetalhes do contato:")
                print(f"Nome completo: {c['nome_contato']} {c['sobrenome_contato']}")
                print(f"Telefone fixo: {c['telefone_fixo']}")
                print(f"Celular: {c['telefone_celular']}")
                print(f"Email: {c['email_contato']}")
                print(f"Data de nascimento: {c['dia_nascimento']}/{c['mes_nascimento']}/{c['ano_nascimento']}")
                achou = True
                break
        if not achou:
            print("Ops! Não achei esse contato na agenda.")

    elif opcao == "4":  
        nome_busca = input("Qual o primeiro nome do contato que quer modificar? ")
        sobrenome_busca = input("E o sobrenome? ")
        contato_encontrado = None
        for c in agenda:
            if c["nome_contato"] == nome_busca and c["sobrenome_contato"] == sobrenome_busca:
                contato_encontrado = c
                break
        if contato_encontrado is None:
            print("Não encontrei esse contato.")
        else:
            while True:
                print("\nQual campo você quer alterar?")
                print("1 - Nome")
                print("2 - Sobrenome")
                print("3 - Telefone fixo")
                print("4 - Celular")
                print("5 - Email")
                print("6 - Mês de nascimento")
                print("7 - Dia de nascimento")
                print("8 - Ano de nascimento")
                print("9 - Voltar ao menu")
                escolha_campo = input("Escolha uma opção: ")

                if escolha_campo == "1":
                    novo = input("Novo nome (só letras, até 20): ")
                    if novo.isalpha() and len(novo) <= 20:
                        contato_encontrado["nome_contato"] = novo
                        print("Nome atualizado!")
                    else:
                        print("Nome inválido, não mudou.")

                elif escolha_campo == "2":
                    novo = input("Novo sobrenome (só letras, até 20): ")
                    if novo.isalpha() and len(novo) <= 20:
                        contato_encontrado["sobrenome_contato"] = novo
                        print("Sobrenome atualizado!")
                    else:
                        print("Sobrenome inválido, não mudou.")

                elif escolha_campo == "3":
                    novo = input("Novo telefone fixo (opcional, só números, até 15): ")
                    if novo == "" or (novo.isdigit() and len(novo) <= 15):
                        contato_encontrado["telefone_fixo"] = novo
                        print("Telefone fixo atualizado!")
                    else:
                        print("Telefone inválido, não mudou.")

                elif escolha_campo == "4":
                    novo = input("Novo celular (só números, até 15): ")
                    if novo.isdigit() and len(novo) <= 15:
                        contato_encontrado["telefone_celular"] = novo
                        print("Celular atualizado!")
                    else:
                        print("Celular inválido, não mudou.")

                elif escolha_campo == "5":
                    novo = input("Novo email: ")
                    if "@" in novo and "." in novo.split("@")[-1]:
                        contato_encontrado["email_contato"] = novo
                        print("Email atualizado!")
                    else:
                        print("Email inválido, não mudou.")

                elif escolha_campo == "6":
                    novo = input("Novo mês de nascimento (1-12): ")
                    if novo.isdigit() and 1 <= int(novo) <= 12:
                        contato_encontrado["mes_nascimento"] = novo
                        print("Mês atualizado!")
                    else:
                        print("Mês inválido, não mudou.")

                elif escolha_campo == "7":
                    novo = input("Novo dia de nascimento (1-31): ")
                    if novo.isdigit() and 1 <= int(novo) <= 31:
                        contato_encontrado["dia_nascimento"] = novo
                        print("Dia atualizado!")
                    else:
                        print("Dia inválido, não mudou.")

                elif escolha_campo == "8":
                    novo = input("Novo ano de nascimento (1900-2025): ")
                    if novo.isdigit() and 1900 <= int(novo) <= 2025:
                        contato_encontrado["ano_nascimento"] = novo
                        print("Ano atualizado!")
                    else:
                        print("Ano inválido, não mudou.")

                elif escolha_campo == "9":
                    print("Voltando ao menu principal...")
                    break
                else:
                    print("Opção inválida, tenta de novo.")

    elif opcao == "5":  
        nome_busca = input("Primeiro nome do contato para apagar: ")
        sobrenome_busca = input("Sobrenome do contato: ")
        removido = False
        for i, c in enumerate(agenda):
            if c["nome_contato"] == nome_busca and c["sobrenome_contato"] == sobrenome_busca:
                del agenda[i]
                print(f"Contato {nome_busca} {sobrenome_busca} removido com sucesso!")
                removido = True
                break
        if not removido:
            print("Não achei esse contato para apagar.")

    elif opcao == "6":
        print("Programa encerrado. Até mais!")
        break

    else:
        print("Essa opção não existe, tente de novo.")
