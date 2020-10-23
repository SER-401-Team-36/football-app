import Money from './Money';

interface LoanRequest {
  id: number;
  requesteeName: string;
  money: Money;
}

export default LoanRequest;
