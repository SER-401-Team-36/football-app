import { sql } from 'slonik';

import LoanRequest from '../../types/LoanRequest';
import connection from '../connection';
import transformLoanRequestRow from './transformLoanRequestRow';

const getAllLoanRequests = async (): Promise<LoanRequest[]> => {
  const rows = await connection.any(sql`
    SELECT loan_request.id, requestee_name, amount, currency
    FROM loan_requests
      INNER JOIN monies
      ON loan_request.money_id = monies.id;
  `);

  return rows.map((row) => transformLoanRequestRow(row));
};

export default getAllLoanRequests;
