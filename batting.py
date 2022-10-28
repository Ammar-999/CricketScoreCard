def innings():
    # Variables in every over
    run = 0
    current_over = 0
    ball_in_over = 6
    extra = 0
    wicket_in_over = 0
    batsman1 = ""
    batsman2 = ""
    striker = ""
    nonStriker = ""
    batsman1 = (input("Batsman on strike: ").upper())
    batsman2 = (input("Non Striker: ").upper())
    striker = batsman1
    nonStriker = batsman2
    while current_over < ball_in_over:
        delivery = (input("enter score: ").upper())
        print (striker)
        # Defining extra balls and runs (wide=Wide, nB=No-Ball, lB=Leg Bye, bye=Bye, oT=Over Throw)
        if delivery.isalpha():
            wide = 0
            nB = 0
            lB = 0
            bye = 0
            oT = 0
            run_on_extra = 0
            if delivery == "wide".upper():
                run_on_extra = int(input("Run On Extra Ball: "))
                current_over += 1
                ball_in_over += 1
                extra += wide + run_on_extra
                run += extra

                if (run_on_extra % 2) != 0:
                    striker, nonStriker = nonStriker, striker
                    print(striker, nonStriker)

                else:
                   continue

                #if striker == batsman1:

            if delivery == "nB".upper():
                run_on_extra = int(input("Run On Extra Ball: "))
                print("FREE HIT!!!")
                free_hit = int(input("Free Hit: "))
                current_over += 1
                ball_in_over += 1
                extra += nB + run_on_extra + free_hit
                run += extra
                if (run_on_extra % 2) != 0:
                    striker, nonStriker = nonStriker, striker
                    print(striker, nonStriker)

                elif (free_hit % 2) != 0:
                    striker, nonStriker = nonStriker, striker
                    print(striker, nonStriker)

                else:
                    continue
            # updating wicket variable when batsman gets out on delivery
            if delivery == "wicket".upper():
                wicket_in_over += 1
                current_over += 1
            # OT, LB & BYE are count as extra run if any, without extra delivery
            if delivery == "oT".upper() or delivery == "lB".upper() or delivery == "bye".upper():
                run_on_extra = int(input("Run On Extra Ball: "))
                current_over += 1
                extra = oT + lB + bye + run_on_extra
                run += extra
                if (run_on_extra % 2) != 0:
                    striker, nonStriker = nonStriker, striker
                    print(striker, nonStriker)

                else:
                    continue

        elif delivery.isnumeric():
            run += int(delivery)
            current_over += 1
            # if int(delivery % 2)!=0:
            #     striker = batsman2


    return print("Run", run, "/", wicket_in_over, "Wicket(s)", "Extra =", extra)

innings()