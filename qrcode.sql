-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 03, 2022 at 08:45 AM
-- Server version: 10.4.20-MariaDB
-- PHP Version: 8.0.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `qrcode`
--

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `user` int(11) DEFAULT NULL,
  `name` varchar(24) CHARACTER SET utf8 DEFAULT NULL,
  `agency` varchar(32) CHARACTER SET utf8 DEFAULT NULL,
  `Phase` varchar(6) CHARACTER SET utf8 DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`user`, `name`, `agency`, `Phase`) VALUES
(370480, 'นายบุญส่ง มีแย้ม', 'Operation 1 TOG', 'Phase2'),
(380701, 'นายกิจจา โกศล', 'Operation 1 TOG', 'Phase1'),
(350159, 'น.ส.สมคิด ยวงลำใย', 'OP1 Phase1 Uncoat DL Mould', 'Phase1'),
(380540, 'น.ส.บุษบา หวานฉ่ำ', 'OP1 Phase1 Uncoat DL Mould', 'Phase1'),
(431708, 'นางอรุณ ไทยทรงธรรม', 'OP1 Phase1 Uncoat DL Mould', 'Phase1'),
(514055, 'น.ส.ศิราณี สนภู่', 'OP1 Phase1 Uncoat DL Mould', 'Phase1'),
(545111, 'นางมะลิ รักหอม', 'OP1 Phase1 Uncoat DL Mould', 'Phase1'),
(597415, 'นายธีระ ต้อนแก้ว', 'OP1 Phase1 Uncoat DL Mould', 'Phase1'),
(597723, 'นายศักดิ์ดา เยื่องเสือ', 'OP1 Phase1 Uncoat DL Mould', 'Phase1'),
(620335, 'น.ส.วนิดา ลูกภูเขียว', 'OP1 Phase1 Uncoat DL Mould', 'Phase1'),
(360218, 'น.ส.บังอร นาคศรีจันทร์', 'OP1 Phase1 Uncoat DL Before Oven', 'Phase1'),
(391028, 'นายณรงค์ศักดิ์ ดีเดิน', 'OP1 Phase1 Uncoat DL Before Oven', 'Phase1'),
(421233, 'น.ส.กัญญา สนธิศรี', 'OP1 Phase1 Uncoat DL Before Oven', 'Phase1'),
(441923, 'นายสมเกียรติ สะมันยี', 'OP1 Phase1 Uncoat DL Before Oven', 'Phase1'),
(534657, 'น.ส.สุรีรัตน์ คนตรง', 'OP1 Phase1 Uncoat DL Before Oven', 'Phase1'),
(555812, 'น.ส.อาภรณ์รัตน์ สว่างศรี', 'OP1 Phase1 Uncoat DL Before Oven', 'Phase1'),
(576839, 'น.ส.วันวิสา คนตรง', 'OP1 Phase1 Uncoat DL Before Oven', 'Phase1'),
(587026, 'นายประสาน ประกาทอง', 'OP1 Phase1 Uncoat DL Before Oven', 'Phase1'),
(587248, 'น.ส.สุริสาย บุตรสีสี', 'OP1 Phase1 Uncoat DL Before Oven', 'Phase1'),
(597581, 'นายธนวัฒน์ เรืองณรงค์', 'OP1 Phase1 Uncoat DL Before Oven', 'Phase1'),
(597724, 'น.ส.ปรียานุช บุญนาดี', 'OP1 Phase1 Uncoat DL Before Oven', 'Phase1'),
(608137, 'นายจำลอง ฉลุนรัมย์', 'OP1 Phase1 Uncoat DL Before Oven', 'Phase1'),
(608222, 'น.ส.สุดาพร แสงดาว', 'OP1 Phase1 Uncoat DL Before Oven', 'Phase1'),
(620155, 'นายพลากร วงศ์คำผิว', 'OP1 Phase1 Uncoat DL Before Oven', 'Phase1'),
(620327, 'นายชุติพนธ์ อินทรทัต', 'OP1 Phase1 Uncoat DL Before Oven', 'Phase1'),
(620328, 'น.ส.นลพรรณ ไชยมา', 'OP1 Phase1 Uncoat DL Before Oven', 'Phase1'),
(630050, 'น.ส.ณัชชา งามเลิศ', 'OP1 Phase1 Uncoat DL Before Oven', 'Phase1'),
(370467, 'นางจำเนียร ดีเดิน', 'OP1 Phase1 Uncoat DL After Oven', 'Phase1'),
(411160, 'น.ส.ประยอม โต๊ะกา', 'OP1 Phase1 Uncoat DL After Oven', 'Phase1');

-- --------------------------------------------------------

--
-- Table structure for table `result`
--

CREATE TABLE `result` (
  `id` int(11) NOT NULL,
  `Date` varchar(255) NOT NULL,
  `Van01` int(255) NOT NULL,
  `Van02` int(255) NOT NULL,
  `Van03` int(255) NOT NULL,
  `Van04` int(255) NOT NULL,
  `Van05` int(255) NOT NULL,
  `Van06` int(255) NOT NULL,
  `Van07` int(255) NOT NULL,
  `Bus01` int(255) NOT NULL,
  `Bus02` int(255) NOT NULL,
  `Bus03` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `result`
--

INSERT INTO `result` (`id`, `Date`, `Van01`, `Van02`, `Van03`, `Van04`, `Van05`, `Van06`, `Van07`, `Bus01`, `Bus02`, `Bus03`) VALUES
(400, '2022-04-28', 0, 0, 0, 0, 0, 0, 0, 0, 1, 0),
(401, '2022-04-28', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0),
(402, '2022-04-28', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `Username` varchar(255) DEFAULT NULL,
  `Container` varchar(255) DEFAULT NULL,
  `Time` varchar(255) DEFAULT NULL,
  `Date` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `Username`, `Container`, `Time`, `Date`) VALUES
(400, '545111', 'Bus02', '14:31:10', '2022-04-28'),
(401, '597415', 'Van01', '14:37:26', '2022-04-28'),
(402, '350159', 'Van01', '14:35:51', '2022-04-28');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `result`
--
ALTER TABLE `result`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `result`
--
ALTER TABLE `result`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=403;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=403;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
