def PMT(rate, nper, pv, fv=0, type=0):
    if rate!= 0:
               pmt = (rate*(fv+pv*(1+ rate)**nper))/((1+rate*type)*(1-(1+ rate)**nper))
    else:
               pmt = (-1*(fv+pv)/nper)
    return(pmt)


def IPMT(rate, per, nper, pv, fv=0, type=0):
  ipmt = -( ((1+rate)**(per-1)) * (pv*rate + PMT(rate, nper, pv, fv=0, type=0)) - PMT(rate, nper,pv, fv=0, type=0))
  return(ipmt)


def PPMT(rate, per, nper, pv, fv=0, type=0):
  ppmt = PMT(rate, nper, pv, fv=0, type=0) - IPMT(rate, per, nper, pv, fv=0, type=0)
  return(ppmt)


loan_amount = 50000
interest = 8.5
interest_rate = interest / 100
loan_term = 6
remaining_balance = loan_amount

for i in range(1, (loan_term*12)+1):
    monthly_installment = PMT(interest_rate / 12, 12 * loan_term, loan_amount)
    principal = PPMT(interest_rate / 12, i, 12 * loan_term, loan_amount)
    interest = IPMT(interest_rate / 12, i, 12 * loan_term, loan_amount)
    print(f'Installment {i}', round(monthly_installment, 2), round(principal, 2), round(interest, 2),
          round(remaining_balance + principal, 2))

    remaining_balance += principal

