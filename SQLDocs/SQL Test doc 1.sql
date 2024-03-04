SELECT * FROM payment;
ALTER TABLE payment
ADD only_date;
SELECT * FROM payment;
SELECT sum(amount), str_to_date(payment_date, '%Y-%m-%d') as datum  FROM sakila.payment group by datum