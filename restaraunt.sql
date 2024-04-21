-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 16, 2024 at 01:34 PM
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
-- Database: `restaraunt`
--

-- --------------------------------------------------------

--
-- Table structure for table `customerdetails`
--

CREATE TABLE `customerdetails` (
  `id` int(100) NOT NULL,
  `name1` varchar(100) NOT NULL,
  `forder` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `deliverdate` datetime(6) NOT NULL,
  `comments` text NOT NULL,
  `regdate` timestamp(6) NOT NULL DEFAULT current_timestamp(6) ON UPDATE current_timestamp(6),
  `Status` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customerdetails`
--

INSERT INTO `customerdetails` (`id`, `name1`, `forder`, `email`, `deliverdate`, `comments`, `regdate`, `Status`) VALUES
(1, 'hari', 'mbriyani', 'harish@123', '2024-04-09 21:10:00.000000', 'I want more spicy!! and yummy!!', '2024-04-10 17:35:02.212997', 'Delivered'),
(2, 'Dhana', 'fried rice', 'dhana@gmail.com', '2024-04-10 09:30:00.000000', 'I want more vegtables to make it !! with spicy', '2024-04-10 17:35:14.939362', 'In progress'),
(3, 'Vinoth', 'cbriyani', 'vinoth12@gmail.com', '2024-04-14 10:30:00.000000', 'I want more quantity of this food!!', '2024-04-12 17:04:22.984250', 'In progress'),
(5, 'jeeva', 'mbriyani', 'jeeva@gmail.com', '2024-04-12 22:36:00.000000', 'Be on time!!', '2024-04-12 17:07:34.121718', 'Delivered'),
(6, 'aswin', 'mbriyani', 'aswin12@gmail.com', '2024-04-13 10:55:00.000000', 'I want more spicy!!', '2024-04-13 05:26:06.184264', ''),
(7, 'hari', 'fried rice', 'harish@123', '2024-04-04 15:11:00.000000', 'I want to delivered on time!!', '2024-04-15 09:41:32.766007', '');

-- --------------------------------------------------------

--
-- Table structure for table `msend`
--

CREATE TABLE `msend` (
  `id` int(100) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `mailid` varchar(100) NOT NULL,
  `mailbox` varchar(100) NOT NULL,
  `regdate` timestamp(6) NOT NULL DEFAULT current_timestamp(6) ON UPDATE current_timestamp(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `msend`
--

INSERT INTO `msend` (`id`, `Name`, `mailid`, `mailbox`, `regdate`) VALUES
(1, 'Vijay', 'harishbalaji123456780@gmail.com', 'Your order is delivering!!', '2024-04-13 06:41:05.734305'),
(2, 'Saravanan', 'harishbalaji123456780@gmail.com', 'Your order is delivered!!,Thanks for your order!! come again', '2024-04-13 06:43:48.137932'),
(10, 'Anju', 'harishbalaji123456780@gmail.com', 'Your order is delivered!!', '2024-04-13 15:46:52.356276'),
(11, 'pirathima', 'techvolt.pirathima@gmail.com', 'Hello!!', '2024-04-16 11:30:54.786030');

-- --------------------------------------------------------

--
-- Table structure for table `profile`
--

CREATE TABLE `profile` (
  `id` int(100) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `dob` date NOT NULL,
  `image` varchar(100) NOT NULL,
  `pass` varchar(100) NOT NULL,
  `regdate` timestamp(6) NOT NULL DEFAULT current_timestamp(6) ON UPDATE current_timestamp(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `profile`
--

INSERT INTO `profile` (`id`, `Name`, `email`, `dob`, `image`, `pass`, `regdate`) VALUES
(1, 'Harishbalaji', 'harishbalaji@gmail.com', '2024-04-11', 'Zomato_logo.png', '', '2024-04-15 16:36:00.846186'),
(2, 'Harishbalaji', 'harishbalaji@gmail.com', '2024-04-11', 'hat.jpg', '', '2024-04-14 14:36:18.925261'),
(3, 'Harishbalaji', 'harishbalaji@gmail.com', '2024-04-11', 'hat.jpg', '', '2024-04-14 14:36:52.292658'),
(4, 'vijay', 'vijay@gmail.com', '2024-04-15', 'bat.jpg', '', '2024-04-14 14:42:13.755449'),
(5, 'Selvan', 'selva@gmail.com', '2024-04-22', 'sat.jpg', '', '2024-04-14 14:54:21.518818'),
(6, 'Selvan', 'selva@gmail.com', '2024-04-22', 'sat.jpg', '', '2024-04-14 15:08:36.608763'),
(7, 'Anju', 'anjana@gmail.com', '2024-04-15', '124569.jpg', '', '2024-04-14 17:18:35.849728'),
(8, 'Sarath', 'sarath@gmail.com', '2024-04-08', '50-Years-Logo-New-01-01.png', '', '2024-04-14 17:20:32.939653'),
(9, 'Dhanalakshmi', 'dhana@gmail.com', '2024-04-10', '124569.jpg', 'dhana12', '2024-04-15 16:28:57.814995'),
(10, 'saravana', 'saravanan@gmail.com', '2024-04-01', 'WorstHead.0.jpg', 'saravana@123', '2024-04-15 16:38:22.207450');

-- --------------------------------------------------------

--
-- Table structure for table `reg_form`
--

CREATE TABLE `reg_form` (
  `id` int(20) NOT NULL,
  `regdate` timestamp(6) NOT NULL DEFAULT current_timestamp(6) ON UPDATE current_timestamp(6),
  `uname` varchar(100) NOT NULL,
  `cemail` varchar(100) NOT NULL,
  `cpsw` varchar(100) NOT NULL,
  `phone` bigint(100) NOT NULL,
  `addr` varchar(100) NOT NULL,
  `pin` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `reg_form`
--

INSERT INTO `reg_form` (`id`, `regdate`, `uname`, `cemail`, `cpsw`, `phone`, `addr`, `pin`) VALUES
(1, '2024-03-25 11:51:36.814842', 'harish', 'harishbalaji@gmail.com', 'Harish16@2024', 9345568050, 'Coimbatore', 641019),
(3, '2024-03-25 11:59:34.277675', 'anu', 'anu@gmail.com', '12345', 8728216311, 'chennai', 600037),
(4, '2024-03-27 12:21:27.734544', 'aswin', 'aswin@gmail.com', 'Test@123', 9198273772, 'madurai', 691021),
(5, '2024-04-04 13:39:42.106826', 'Tittu', 'tittu@gmail.com', 'Tittu@123', 9198273771, 'trichangode', 691021),
(6, '2024-04-05 11:35:53.260636', 'dhanam', 'dhana@gmail.com', 'dhana@123', 9198273771, 'trichy', 600037),
(11, '2024-04-08 10:55:42.278760', 'anju', 'anju@gmail.com', 'anju123', 934559023, 'kerala', 710191),
(12, '2024-04-15 15:55:12.908196', 'aravind', 'aravind12@gmail.com', 'aravind', 8728216312, 'madurai', 641012),
(13, '2024-04-15 16:00:13.572455', 'aravind', 'aravind12@gmail.com', 'aravind', 8728216312, 'madurai', 641012);

-- --------------------------------------------------------

--
-- Table structure for table `userlogin`
--

CREATE TABLE `userlogin` (
  `id` int(100) NOT NULL,
  `usern` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `dob` varchar(30) NOT NULL,
  `passw` varchar(100) NOT NULL,
  `phn` bigint(10) NOT NULL,
  `address` varchar(100) NOT NULL,
  `pincode` int(10) NOT NULL,
  `regdate` timestamp(6) NOT NULL DEFAULT current_timestamp(6) ON UPDATE current_timestamp(6),
  `image` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `userlogin`
--

INSERT INTO `userlogin` (`id`, `usern`, `email`, `dob`, `passw`, `phn`, `address`, `pincode`, `regdate`, `image`) VALUES
(1, 'aswin', 'aswin@gmail.com', '', '1222', 9198273772, 'chennai', 600038, '2024-04-16 11:20:24.597262', '124569.jpg'),
(2, 'Dhanalakshmi', 'dhana@gmail.com', '', 'dhana@123', 9845567123, 'Erode', 641011, '2024-04-09 16:14:02.942704', ''),
(4, 'anju', 'anju@gmail.com', '', 'anju12', 9345568021, 'wayanadu', 641012, '2024-04-10 15:38:45.936561', ''),
(5, 'saravana', 'saravanan@gmail.com', '', 'sara', 9345568050, 'trichy', 641012, '2024-04-15 16:33:43.994138', ''),
(6, 'aswin', 'aswin@gmail.com', '2024-04-16', 'aswin12', 0, '', 0, '2024-04-16 10:07:17.372740', '124569.jpg'),
(7, 'aswin', 'aswin@gmail.com', '2024-04-16', 'aswin12', 0, '', 0, '2024-04-16 10:10:18.950679', '124569.jpg'),
(8, 'aswin', 'aswin@gmail.com', '2024-04-16', 'aswin12', 0, '', 0, '2024-04-16 10:14:19.603854', '124569.jpg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customerdetails`
--
ALTER TABLE `customerdetails`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `msend`
--
ALTER TABLE `msend`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `profile`
--
ALTER TABLE `profile`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `reg_form`
--
ALTER TABLE `reg_form`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `userlogin`
--
ALTER TABLE `userlogin`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customerdetails`
--
ALTER TABLE `customerdetails`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `msend`
--
ALTER TABLE `msend`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `profile`
--
ALTER TABLE `profile`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `reg_form`
--
ALTER TABLE `reg_form`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `userlogin`
--
ALTER TABLE `userlogin`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
