


print("khosh amadid")

while True:

    gozineha=input("1.kharide mahsool 2.hazfe mahsool 3.soorat hesab:")

    kala=[]
    factor=[]
    while True:
        match gozineha:
            case "1":
                pooshak=["shalvar","tshirt","katooni"]
                gheymat=["2000","1000","3000"]

                print("1.shalvar 2.tshirt katooni")

                entekhab=input("che poshaki mikhahid?name pooshak ra benevis:")
                if entekhab=="shalvar":
                    tedad_shalvar=int(input("che tedad mikhahid?:"))
                    gheymat_shalvar=tedad_shalvar*2000*1.1
                    print(gheymat_shalvar)
                    kala.append("shalvar")
                    factor.append(gheymat_shalvar)
                    continue

                elif entekhab=="tshirt":
                    tedad_tshirt=int(input("che tedad mikhahid?:"))
                    gheymat_tshirt=tedad_tshirt*1000*1.1
                    print(gheymat_tshirt)
                    kala.append("tshirt")
                    factor.append(gheymat_tshirt)
                    continue

                elif entekhab=="katooni":
                    tedad_katooni=int(input("che tedad mikhahid?:"))
                    gheymat_katooni=tedad_katooni*3000*1.1
                    print(gheymat_katooni)
                    kala.append("katooni")
                    factor.append(gheymat_katooni)
                    break
            case "2":
                print(kala)
                hazf_mahsool=input("kodam mahsool hazf shavad?: ")
                if hazf_mahsool=="shalvar":
                    kala.remove("shalvar")
                    factor.remove(gheymat_shalvar)
                    print(kala)
                    print(factor)
                
                elif hazf_mahsool=="tshirt":
                    kala.remove("tshirt")
                    factor.remove(gheymat_tshirt)
                    print(kala)
                    print(factor)

                elif hazf_mahsool=="katooni":
                    kala.remove("katooni")
                    factor.remove(gheymat_katooni) 
                    print(kala)       
                    print(factor)
                    break

            case "3":
                factor_nahaie=sum(factor)
                print(factor_nahaie)
        break




            

                    

