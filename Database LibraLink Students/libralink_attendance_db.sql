-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 22, 2023 at 05:53 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `libralink_attendance_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `Department` varchar(45) NOT NULL,
  `Course` varchar(45) NOT NULL,
  `Year` varchar(45) NOT NULL,
  `Semester` int(11) NOT NULL,
  `StudentID` varchar(45) NOT NULL,
  `StudentName` varchar(45) NOT NULL,
  `ClassDivision` varchar(45) NOT NULL,
  `Gender` varchar(45) DEFAULT NULL,
  `DateOfBirth` date DEFAULT NULL,
  `Email` varchar(45) DEFAULT NULL,
  `PhoneNumber` varchar(45) DEFAULT NULL,
  `Address` varchar(45) DEFAULT NULL,
  `PhotoSample` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`Department`, `Course`, `Year`, `Semester`, `StudentID`, `StudentName`, `ClassDivision`, `Gender`, `DateOfBirth`, `Email`, `PhoneNumber`, `Address`, `PhotoSample`) VALUES
('School of Computer Science', 'Computer Science', '2022/2023', 3, '2602115788', 'Franco Antonio Pranata', 'LA', 'Male', '2004-09-24', NULL, NULL, 'SMG', 'Yes'),
('School of Computer Science', 'Computer Science', '2022/2023', 3, '2602238021', 'Michael Geraldin Wijaya', 'LA', 'Male', '2004-03-24', 'michaelwjy2@gmail.com', '62895604339001', 'Kos Bu Joko Kamar A', 'Yes');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`StudentID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
