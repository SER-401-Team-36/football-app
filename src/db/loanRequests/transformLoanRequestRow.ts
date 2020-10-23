import LoanRequest from '../../types/LoanRequest';
import Money from '../../types/Money';

export interface LoanRequestRow {
  id: number;
  requestee_name: string;
  units: number;
  currency: Money['currency'];
}

const transformLoanRequestRow = (row: LoanRequestRow): LoanRequest => {
  return {
    id: row.id,
    requesteeName: row.requestee_name,
    money: {
      units: row.units,
      currency: row.currency,
    },
  };
};

export default transformLoanRequestRow;
