-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th5 29, 2023 lúc 09:03 AM
-- Phiên bản máy phục vụ: 10.4.28-MariaDB
-- Phiên bản PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `datn`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `accs_hist`
--

CREATE TABLE `accs_hist` (
  `accs_id` int(11) NOT NULL,
  `accs_date` date NOT NULL,
  `accs_prsn` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `accs_added` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `class`
--

CREATE TABLE `class` (
  `id` int(11) NOT NULL,
  `name_class` varchar(100) NOT NULL,
  `course` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `class`
--

INSERT INTO `class` (`id`, `name_class`, `course`) VALUES
(13, 'Lập trình game', 'HKI 2022-2023'),
(15, 'Nguyên lý lập trình cấu trúc', 'HKI 2022-2023');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `img_dataset`
--

CREATE TABLE `img_dataset` (
  `img_id` int(11) NOT NULL,
  `img_sv` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Đang đổ dữ liệu cho bảng `img_dataset`
--

INSERT INTO `img_dataset` (`img_id`, `img_sv`) VALUES
(1, '2115217'),
(2, '2115217'),
(3, '2115217'),
(4, '2115217'),
(5, '2115217'),
(6, '2115217'),
(7, '2115217'),
(8, '2115217'),
(9, '2115217'),
(10, '2115217'),
(11, '2115217'),
(12, '2115217'),
(13, '2115217'),
(14, '2115217'),
(15, '2115217'),
(16, '2115217'),
(17, '2115217'),
(18, '2115217'),
(19, '2115217'),
(20, '2115217'),
(21, '2115196'),
(22, '2115196'),
(23, '2115196'),
(24, '2115196'),
(25, '2115196'),
(26, '2115196'),
(27, '2115196'),
(28, '2115196'),
(29, '2115196'),
(30, '2115196'),
(31, '2115196'),
(32, '2115196'),
(33, '2115196'),
(34, '2115196'),
(35, '2115196'),
(36, '2115196'),
(37, '2115196'),
(38, '2115196'),
(39, '2115196'),
(40, '2115196'),
(41, '2116969'),
(42, '2116969'),
(43, '2116969'),
(44, '2116969'),
(45, '2116969'),
(46, '2116969'),
(47, '2116969'),
(48, '2116969'),
(49, '2116969'),
(50, '2116969'),
(51, '2116969'),
(52, '2116969'),
(53, '2116969'),
(54, '2116969'),
(55, '2116969'),
(56, '2116969'),
(57, '2116969'),
(58, '2116969'),
(59, '2116969'),
(60, '2116969'),
(61, '2116976'),
(62, '2116976'),
(63, '2116976'),
(64, '2116976'),
(65, '2116976'),
(66, '2116976'),
(67, '2116976'),
(68, '2116976'),
(69, '2116976'),
(70, '2116976'),
(71, '2116976'),
(72, '2116976'),
(73, '2116976'),
(74, '2116976'),
(75, '2116976'),
(76, '2116976'),
(77, '2116976'),
(78, '2116976'),
(79, '2116976'),
(80, '2116976'),
(81, '2115243'),
(82, '2115243'),
(83, '2115243'),
(84, '2115243'),
(85, '2115243'),
(86, '2115243'),
(87, '2115243'),
(88, '2115243'),
(89, '2115243'),
(90, '2115243'),
(91, '2115243'),
(92, '2115243'),
(93, '2115243'),
(94, '2115243'),
(95, '2115243'),
(96, '2115243'),
(97, '2115243'),
(98, '2115243'),
(99, '2115243'),
(100, '2115243'),
(101, '2115200'),
(102, '2115200'),
(103, '2115200'),
(104, '2115200'),
(105, '2115200'),
(106, '2115200'),
(107, '2115200'),
(108, '2115200'),
(109, '2115200'),
(110, '2115200'),
(111, '2115200'),
(112, '2115200'),
(113, '2115200'),
(114, '2115200'),
(115, '2115200'),
(116, '2115200'),
(117, '2115200'),
(118, '2115200'),
(119, '2115200'),
(120, '2115200'),
(121, '2115200'),
(122, '2115200'),
(123, '2115200'),
(124, '2115200'),
(125, '2115232'),
(126, '2115232'),
(127, '2115232'),
(128, '2115232'),
(129, '2115232'),
(130, '2115232'),
(131, '2115232'),
(132, '2115232'),
(133, '2115232'),
(134, '2115232'),
(135, '2115232'),
(136, '2115232'),
(137, '2115232'),
(138, '2115232'),
(139, '2115232'),
(140, '2115232'),
(141, '2115232'),
(142, '2115232'),
(143, '2115232'),
(144, '2115232'),
(145, '2115232'),
(146, '2115232'),
(147, '2115232'),
(148, '2115232'),
(149, '2115234'),
(150, '2115234'),
(151, '2115234'),
(152, '2115234'),
(153, '2115234'),
(154, '2115234'),
(155, '2115234'),
(156, '2115234'),
(157, '2115234'),
(158, '2115234'),
(159, '2115234'),
(160, '2115234'),
(161, '2115234'),
(162, '2115234'),
(163, '2115234'),
(164, '2115234'),
(165, '2115234'),
(166, '2115234'),
(167, '2115234'),
(168, '2115234'),
(169, '2115234'),
(170, '2115236'),
(171, '2115236'),
(172, '2115236'),
(173, '2115236'),
(174, '2115236'),
(175, '2115236'),
(176, '2115236'),
(177, '2115236'),
(178, '2115236'),
(179, '2115236'),
(180, '2115236'),
(181, '2115236'),
(182, '2115236'),
(183, '2115236'),
(184, '2115236'),
(185, '2115236'),
(186, '2115236'),
(187, '2115236'),
(188, '2115236'),
(189, '2115236'),
(190, '2115236'),
(191, '2115236'),
(192, '2115236'),
(193, '2115236'),
(194, '2115274'),
(195, '2115274'),
(196, '2115274'),
(197, '2115274'),
(198, '2115274'),
(199, '2115274'),
(200, '2115274'),
(201, '2115274'),
(202, '2115274'),
(203, '2115274'),
(204, '2115274'),
(205, '2115274'),
(206, '2115274'),
(207, '2115274'),
(208, '2115274'),
(209, '2115274'),
(210, '2115274'),
(211, '2115274'),
(212, '2115274'),
(213, '2115274'),
(214, '2115274'),
(215, '2115270'),
(216, '2115270'),
(217, '2115270'),
(218, '2115270'),
(219, '2115270'),
(220, '2115270'),
(221, '2115270'),
(222, '2115270'),
(223, '2115270'),
(224, '2115270'),
(225, '2115270'),
(226, '2115270'),
(227, '2115270'),
(228, '2115270'),
(229, '2115270'),
(230, '2115270'),
(231, '2115270'),
(232, '2115270'),
(233, '2115270'),
(234, '2115270'),
(235, '2115270'),
(236, '2115270'),
(237, '2115270'),
(238, '2115270'),
(239, '2115227'),
(240, '2115227'),
(241, '2115227'),
(242, '2115227'),
(243, '2115227'),
(244, '2115227'),
(245, '2115227'),
(246, '2115227'),
(247, '2115227'),
(248, '2115227'),
(249, '2115227'),
(250, '2115227'),
(251, '2115227'),
(252, '2115227'),
(253, '2115227'),
(254, '2115227'),
(255, '2115227'),
(256, '2115227'),
(257, '2115227'),
(258, '2115227'),
(259, '2115201'),
(260, '2115201'),
(261, '2115201'),
(262, '2115201'),
(263, '2115201'),
(264, '2115201'),
(265, '2115201'),
(266, '2115201'),
(267, '2115201'),
(268, '2115201'),
(269, '2115201'),
(270, '2115201'),
(271, '2115201'),
(272, '2115201'),
(273, '2115201'),
(274, '2115201'),
(275, '2115201'),
(276, '2115201'),
(277, '2115201'),
(278, '2115201'),
(329, '2115207'),
(330, '2115207'),
(331, '2115207'),
(332, '2115207'),
(333, '2115207'),
(334, '2115207'),
(335, '2115207'),
(336, '2115207'),
(337, '2115207'),
(338, '2115207'),
(339, '2115207'),
(340, '2115207'),
(341, '2115207'),
(342, '2115207'),
(343, '2115207'),
(344, '2115207'),
(345, '2115207'),
(346, '2115207'),
(347, '2115207'),
(348, '2115207'),
(349, '2115207'),
(350, '2115207'),
(351, '2115207'),
(352, '2115207'),
(353, '1911160'),
(354, '1911160'),
(355, '1911160'),
(356, '1911160'),
(357, '1911160'),
(358, '1911160'),
(359, '1911160'),
(360, '1911160'),
(361, '1911160'),
(362, '1911160'),
(363, '1911160'),
(364, '1911160'),
(365, '1911160'),
(366, '1911160'),
(367, '1911160'),
(368, '1911160'),
(369, '1911160'),
(370, '1911160'),
(371, '1911160'),
(372, '1911160'),
(373, '1911160'),
(374, '1911160'),
(375, '1911160'),
(376, '1911160'),
(377, '1911160'),
(378, '1911160'),
(379, '1911160'),
(380, '1911160'),
(381, '1911160'),
(382, '1911160'),
(383, '1911160'),
(384, '1911160'),
(385, '1911160'),
(386, '1911160'),
(387, '1911160'),
(388, '1911160'),
(389, '1911160'),
(390, '1911160'),
(391, '1911160'),
(392, '1911160'),
(393, '1911160'),
(394, '1911160'),
(395, '1911160'),
(396, '1911160'),
(397, '1911160'),
(398, '1911160'),
(399, '1911160'),
(400, '1911160'),
(401, '1911160'),
(402, '1911160');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `qlsv`
--

CREATE TABLE `qlsv` (
  `mssv` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `sv_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `sv_class` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `sv_active` varchar(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT 'Y',
  `sv_added` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Đang đổ dữ liệu cho bảng `qlsv`
--

INSERT INTO `qlsv` (`mssv`, `sv_name`, `email`, `sv_class`, `sv_active`, `sv_added`) VALUES
('1911160', 'Phan Trung Kiên', '1911160@dlu.edu.vn', 'CTK43', 'Y', '2023-05-28 19:59:09'),
('2115196', 'Dau Thi Tieu Diep', '2115196@dlu.edu.vn', 'CTK45', 'Y', '2023-05-26 12:30:41'),
('2115200', 'Luong Tuan Duy', '2115200@dlu.edu.vn', 'CTK45', 'Y', '2023-05-26 12:38:46'),
('2115201', 'Vy Nhat Duy', '2115201@dlu.edu.vn', 'CTK45', 'Y', '2023-05-26 13:04:11'),
('2115207', 'Dinh Trong Hieu', '2115207@dlu.edu.vn', 'CTK45', 'Y', '2023-05-28 19:53:20'),
('2115217', 'Huỳnh Thị Thảo Hương', '2115217@dlu.edu.vn', 'CTK45', 'Y', '2023-05-26 12:29:20'),
('2115227', 'Truong Thanh Lam', '2115227@dlu.edu.vn', 'CTK45', 'Y', '2023-05-26 12:57:26'),
('2115232', 'Nguyen Duc Dai Loc', '2115232@dlu.edu.vn', 'CTK45', 'Y', '2023-05-26 12:41:53'),
('2115234', 'Nguyen Thanh Long', '2115234@dlu.edu.vn', 'CTK45', 'Y', '2023-05-26 12:44:19'),
('2115236', 'Nguyễn Thị Trúc Mai', '2115236@dlu.edu.vn', 'CTK45', 'Y', '2023-05-26 12:47:01'),
('2115243', 'Lai Phu Khoi Nguyen', '2115243@dlu.edu.vn', 'CTK45', 'Y', '2023-05-26 12:37:28'),
('2115270', 'Tran Trung Thanh', '2115270@dlu.edu.vn', 'CTK45', 'Y', '2023-05-26 12:55:09'),
('2115274', 'Nguyen Xuan Tien', '2115274@dlu.edu.vn', 'CTK45', 'Y', '2023-05-26 12:50:02'),
('2116969', 'Bui Xuan Quy', '2116969@dlu.edu.vn', 'CTK45', 'Y', '2023-05-26 12:32:08'),
('2116976', 'Bui Minh Lien', '2116976@dlu.edu.vn', 'CTK45', 'Y', '2023-05-26 12:33:53');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `studentclass`
--

CREATE TABLE `studentclass` (
  `id` int(11) NOT NULL,
  `mssv` varchar(10) NOT NULL,
  `idclass` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `studentclass`
--

INSERT INTO `studentclass` (`id`, `mssv`, `idclass`) VALUES
(462, '1911160', 13),
(466, '2115196', 13),
(468, '2115227', 13),
(469, '1911160', 15),
(470, '2115196', 15),
(471, '2115200', 15);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` char(102) NOT NULL,
  `fullname` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `user`
--

INSERT INTO `user` (`id`, `email`, `password`, `fullname`) VALUES
(1, 'admin@dlu.edu.vn', 'pbkdf2:sha256:260000$LOGdICmP4g4pSTor$af0dc7adafb778ef4b1d4eb112511aa24869f138b4a121ceec2d4b1933c84f6c', 'Admin');

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `accs_hist`
--
ALTER TABLE `accs_hist`
  ADD PRIMARY KEY (`accs_id`),
  ADD KEY `accs_date` (`accs_date`);

--
-- Chỉ mục cho bảng `class`
--
ALTER TABLE `class`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `img_dataset`
--
ALTER TABLE `img_dataset`
  ADD PRIMARY KEY (`img_id`);

--
-- Chỉ mục cho bảng `qlsv`
--
ALTER TABLE `qlsv`
  ADD PRIMARY KEY (`mssv`);

--
-- Chỉ mục cho bảng `studentclass`
--
ALTER TABLE `studentclass`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `accs_hist`
--
ALTER TABLE `accs_hist`
  MODIFY `accs_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=67;

--
-- AUTO_INCREMENT cho bảng `class`
--
ALTER TABLE `class`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT cho bảng `studentclass`
--
ALTER TABLE `studentclass`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=472;

--
-- AUTO_INCREMENT cho bảng `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
