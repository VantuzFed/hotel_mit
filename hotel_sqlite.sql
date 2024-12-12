CREATE TABLE "clients" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  "first_name" TEXT NOT NULL,
  "middle_name" TEXT DEFAULT NULL,
  "last_name" TEXT NOT NULL,
  "e_mail" TEXT DEFAULT NULL,
  "phone_number" TEXT NOT NULL,
  "document_id" TEXT NOT NULL
);

CREATE TABLE "employees" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  "first_name" TEXT NOT NULL,
  "middle_name" TEXT DEFAULT NULL,
  "last_name" TEXT NOT NULL
);

CREATE TABLE "rooms" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  "room_number" TEXT NOT NULL,
  "class" TEXT NOT NULL,
  "price_per_day" INTEGER NOT NULL,
  "available" INTEGER DEFAULT 1
);

CREATE TABLE "booking" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  "room_id" INTEGER NOT NULL,
  "book_start" TEXT NOT NULL,
  "book_end" TEXT NOT NULL,
  "book_status" TEXT DEFAULT 'Начало',
  FOREIGN KEY ("room_id") REFERENCES "rooms"("id")
);

CREATE TABLE "bill" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  "book_id" INTEGER NOT NULL,
  "emp_id" INTEGER NOT NULL,
  "client_id" INTEGER NOT NULL,
  "pice_total" INTEGER DEFAULT NULL,
  FOREIGN KEY ("book_id") REFERENCES "booking"("id"),
  FOREIGN KEY ("emp_id") REFERENCES "employees"("id"),
  FOREIGN KEY ("client_id") REFERENCES "clients"("id")
);

CREATE TABLE "job_history" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  "emp_id" INTEGER NOT NULL,
  "occupation" TEXT NOT NULL,
  "salary" INTEGER NOT NULL,
  "start_date" TEXT NOT NULL,
  "end_date" TEXT DEFAULT NULL,
  FOREIGN KEY ("emp_id") REFERENCES "employees"("id")
);
