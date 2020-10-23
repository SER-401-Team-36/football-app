import LoanRequest from '../../types/LoanRequest';
import Money from '../../types/Money';

interface LoanRequestRow {
  id: number;
  requestee_name: string;
  amount: number;
  currency: Money['currency'];
}

const transformLoanRequestRow = (row: LoanRequestRow): LoanRequest => {
  return {
    id: row.id,
    requesteeName: row.requestee_name,
    money: {
      amount: row.amount,
      currency: row.currency,
    },
  };
};

export default transformLoanRequestRow;
