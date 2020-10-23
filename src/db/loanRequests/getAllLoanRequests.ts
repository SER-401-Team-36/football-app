import { sql } from 'slonik';

import LoanRequest from '../../types/LoanRequest';
import connection from '../connection';
import transformLoanRequestRow, { LoanRequestRow } from './transformLoanRequestRow';

const getAllLoanRequests = async (): Promise<LoanRequest[]> => {
  const rows = await connection.any<LoanRequestRow>(sql`
    SELECT loan_requests.id, requestee_name, units, currency
    FROM loan_requests
      INNER JOIN monies
      ON loan_requests.money_id = monies.id;
  `);

  return rows.map((row) => transformLoanRequestRow(row));
};

export default getAllLoanRequests;
