-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 06, 2021 at 10:41 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.2.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pettu_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin_sellerapp_add_category`
--

CREATE TABLE `admin_sellerapp_add_category` (
  `cat_id` int(11) NOT NULL,
  `category_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin_sellerapp_add_category`
--

INSERT INTO `admin_sellerapp_add_category` (`cat_id`, `category_name`) VALUES
(1, 'Vegitable'),
(2, 'Fruits'),
(3, 'Stationary'),
(4, 'Fish & Meat'),
(5, 'Dairy & Bakery'),
(6, 'Snaks & Branded Foods');

-- --------------------------------------------------------

--
-- Table structure for table `admin_sellerapp_approval`
--

CREATE TABLE `admin_sellerapp_approval` (
  `approval_id` int(11) NOT NULL,
  `sellerstate` varchar(30) NOT NULL,
  `email` varchar(100) NOT NULL,
  `seller_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add user_reg', 7, 'add_user_reg'),
(26, 'Can change user_reg', 7, 'change_user_reg'),
(27, 'Can delete user_reg', 7, 'delete_user_reg'),
(28, 'Can view user_reg', 7, 'view_user_reg'),
(29, 'Can add seller_reg', 8, 'add_seller_reg'),
(30, 'Can change seller_reg', 8, 'change_seller_reg'),
(31, 'Can delete seller_reg', 8, 'delete_seller_reg'),
(32, 'Can view seller_reg', 8, 'view_seller_reg'),
(33, 'Can add approval', 9, 'add_approval'),
(34, 'Can change approval', 9, 'change_approval'),
(35, 'Can delete approval', 9, 'delete_approval'),
(36, 'Can view approval', 9, 'view_approval'),
(37, 'Can add add_category', 10, 'add_add_category'),
(38, 'Can change add_category', 10, 'change_add_category'),
(39, 'Can delete add_category', 10, 'delete_add_category'),
(40, 'Can view add_category', 10, 'view_add_category'),
(41, 'Can add product', 11, 'add_product'),
(42, 'Can change product', 11, 'change_product'),
(43, 'Can delete product', 11, 'delete_product'),
(44, 'Can view product', 11, 'view_product');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$216000$HH8xKWinLX52$JGfVv8UgQZvNt0m+OSoDsHpuZRGUEOOL7tHPdeJY1nA=', '2021-07-13 14:32:07.833553', 0, 'abhi@gmail.com', 'user', '', '', 0, 1, '2021-05-25 15:39:01.359469'),
(3, 'pbkdf2_sha256$216000$TvBfQju0Wll9$39/Qfz2VQ0QrnbwsfYH0oHLiA7ofR6vFJY8v+frOVQw=', '2021-06-08 15:16:13.089001', 0, 'raju@gmail.com', 'seller', '', '', 0, 1, '2021-05-25 16:01:02.701045'),
(4, 'pbkdf2_sha256$216000$SqKXiVb7eOsO$xGaXz02gXTdp7N/spsPH8Zfnq9W7zgbfo3oOT1Fa9x8=', '2021-05-26 14:55:30.522389', 0, 'admin@gmail.com', 'admin', '', '', 0, 1, '2021-05-26 14:28:31.137766'),
(5, 'pbkdf2_sha256$216000$gJcUI2br5vZN$iLM1HerZIAM7C6SeEePNSs1bPfj3RWWGL5jdtYFUXi0=', '2021-07-20 13:40:24.846858', 0, 'kiran@gmail.com', 'seller', '', '', 0, 1, '2021-05-26 16:34:04.929674'),
(6, 'pbkdf2_sha256$216000$pICHGGtiv6uu$DxIncuVghQLKWQM3PvVzTMetBrl+Dr75NOfskQHXUqk=', NULL, 0, 'rithin@gmail.com', 'user', '', '', 0, 1, '2021-05-26 16:37:35.862739'),
(7, 'pbkdf2_sha256$216000$9F5To1JmJkss$rrcLnV7TMnyncbCPI0fllihLHNwtpF/uDKnZZtv+cYs=', '2021-07-15 15:45:01.424494', 0, 'arya@gmail.com', 'seller', '', '', 0, 1, '2021-05-26 16:42:23.187173'),
(8, 'pbkdf2_sha256$216000$mKGjKx8sM0SV$/wlKz63v3OKhej4LflYO3u3Nr7034DzbKCrpC+xLtQ4=', '2021-07-16 11:16:02.633452', 0, 'moncy@gmail.com', 'seller', '', '', 0, 1, '2021-06-09 08:59:37.700885'),
(10, 'pbkdf2_sha256$216000$15aYonJuvFBz$TFQr7+u1d1zwk1SfTZEqQa5tRtgOqaHKgUe/YkkI+IY=', '2021-07-16 10:38:44.430737', 0, 'jon@gmail.com', 'seller', '', '', 0, 1, '2021-06-13 13:25:28.472555'),
(11, 'pbkdf2_sha256$216000$ZWut43a3GEyU$+cURTLYH8Zf0L5ZoSuBPknz6O+1jp+u58QtDJNrfzLo=', '2021-07-16 10:44:30.841225', 0, 'nikhil@gmail.com', 'seller', '', '', 0, 1, '2021-06-16 13:09:36.530279');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(10, 'admin_sellerapp', 'add_category'),
(9, 'admin_sellerapp', 'approval'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(8, 'homeapp', 'seller_reg'),
(7, 'homeapp', 'user_reg'),
(11, 'productsapp', 'product'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-05-25 15:35:36.465749'),
(2, 'auth', '0001_initial', '2021-05-25 15:35:38.929890'),
(3, 'admin', '0001_initial', '2021-05-25 15:35:48.660447'),
(4, 'admin', '0002_logentry_remove_auto_add', '2021-05-25 15:35:52.172648'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2021-05-25 15:35:52.251652'),
(6, 'admin_sellerapp', '0001_initial', '2021-05-25 15:35:52.906690'),
(7, 'admin_sellerapp', '0002_remove_approval_password', '2021-05-25 15:35:54.834800'),
(8, 'admin_sellerapp', '0003_auto_20210506_1612', '2021-05-25 15:35:55.093815'),
(9, 'contenttypes', '0002_remove_content_type_name', '2021-05-25 15:35:56.408890'),
(10, 'auth', '0002_alter_permission_name_max_length', '2021-05-25 15:35:58.860030'),
(11, 'auth', '0003_alter_user_email_max_length', '2021-05-25 15:35:59.008039'),
(12, 'auth', '0004_alter_user_username_opts', '2021-05-25 15:35:59.071042'),
(13, 'auth', '0005_alter_user_last_login_null', '2021-05-25 15:36:00.414119'),
(14, 'auth', '0006_require_contenttypes_0002', '2021-05-25 15:36:00.512125'),
(15, 'auth', '0007_alter_validators_add_error_messages', '2021-05-25 15:36:00.603130'),
(16, 'auth', '0008_alter_user_username_max_length', '2021-05-25 15:36:00.769139'),
(17, 'auth', '0009_alter_user_last_name_max_length', '2021-05-25 15:36:00.927148'),
(18, 'auth', '0010_alter_group_name_max_length', '2021-05-25 15:36:01.267168'),
(19, 'auth', '0011_update_proxy_permissions', '2021-05-25 15:36:01.354173'),
(20, 'auth', '0012_alter_user_first_name_max_length', '2021-05-25 15:36:01.600187'),
(21, 'homeapp', '0001_initial', '2021-05-25 15:36:02.005210'),
(22, 'homeapp', '0002_auto_20210110_2138', '2021-05-25 15:36:02.968265'),
(23, 'homeapp', '0003_auto_20210110_2141', '2021-05-25 15:36:04.784369'),
(24, 'homeapp', '0004_auto_20210110_2151', '2021-05-25 15:36:06.334458'),
(25, 'homeapp', '0005_user_reg_user_id', '2021-05-25 15:36:08.001553'),
(26, 'homeapp', '0006_seller_reg', '2021-05-25 15:36:08.349573'),
(27, 'homeapp', '0007_auto_20210410_2102', '2021-05-25 15:36:12.052785'),
(28, 'homeapp', '0008_auto_20210413_2013', '2021-05-25 15:36:16.135018'),
(29, 'homeapp', '0009_seller_reg_sellerstate', '2021-05-25 15:36:16.375032'),
(30, 'productsapp', '0001_initial', '2021-05-25 15:36:16.833058'),
(31, 'sessions', '0001_initial', '2021-05-25 15:36:20.310257'),
(32, 'homeapp', '0010_user_reg_u_email', '2021-06-05 14:52:36.867582'),
(33, 'productsapp', '0002_auto_20210605_2022', '2021-06-05 14:52:37.092595'),
(34, 'productsapp', '0003_auto_20210605_2032', '2021-06-05 15:02:09.136314'),
(35, 'productsapp', '0004_auto_20210605_2040', '2021-06-05 15:10:53.008278'),
(36, 'productsapp', '0005_auto_20210616_1835', '2021-06-16 13:05:50.564355'),
(37, 'productsapp', '0006_auto_20210616_1956', '2021-06-16 14:26:58.634792'),
(38, 'productsapp', '0007_auto_20210616_2003', '2021-06-16 14:33:37.940631'),
(39, 'productsapp', '0008_auto_20210616_2007', '2021-06-16 14:37:51.150114'),
(40, 'productsapp', '0009_auto_20210616_2028', '2021-06-16 14:58:12.143951'),
(41, 'productsapp', '0002_auto_20210616_2044', '2021-06-16 15:14:14.987022'),
(42, 'productsapp', '0003_auto_20210616_2106', '2021-06-16 15:36:24.681076');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('rkrniksg4cykhu1uveyznnq2t4wh5gpu', '.eJxVjDsOwyAQRO9CHSE-BpaU6X0GtMASnERYMnYV5e6xJRdJN5r3Zt4s4LbWsHVawpTZlQG7_HYR05PaAfID233maW7rMkV-KPyknY9zptftdP8OKva6rwVo470xyoM14DQ5LA7Q22Sk0EADScgqibxHrSgPzkcJUdoSFZWE7PMFsPw3ag:1m4Lp4:gxkwVq2ERjLz4bHdtCgpLrKq19byRwMdT274sO0oX-g', '2021-07-30 11:16:02.738966');

-- --------------------------------------------------------

--
-- Table structure for table `homeapp_seller_reg`
--

CREATE TABLE `homeapp_seller_reg` (
  `s_id` int(11) NOT NULL,
  `s_fullname` varchar(200) NOT NULL,
  `s_shopname` varchar(200) NOT NULL,
  `s_address` varchar(200) NOT NULL,
  `s_location` varchar(200) NOT NULL,
  `s_coverphoto` varchar(100) NOT NULL,
  `s_profilepic` varchar(100) NOT NULL,
  `s_phone` varchar(10) NOT NULL,
  `s_aadhaar` varchar(15) NOT NULL,
  `s_idproof` varchar(100) NOT NULL,
  `s_gstno` varchar(15) NOT NULL,
  `s_pincode` varchar(6) NOT NULL,
  `s_state` varchar(100) NOT NULL,
  `s_district` varchar(100) NOT NULL,
  `s_taluk` varchar(100) NOT NULL,
  `s_email` varchar(100) NOT NULL,
  `seller_id_id` int(11) NOT NULL,
  `sellerstate` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `homeapp_seller_reg`
--

INSERT INTO `homeapp_seller_reg` (`s_id`, `s_fullname`, `s_shopname`, `s_address`, `s_location`, `s_coverphoto`, `s_profilepic`, `s_phone`, `s_aadhaar`, `s_idproof`, `s_gstno`, `s_pincode`, `s_state`, `s_district`, `s_taluk`, `s_email`, `seller_id_id`, `sellerstate`) VALUES
(2, 'Raju', 'K&k Shop', 'smg muncipl', 'kottaym', 'coverphoto/shop_pic2.jpg', 'profilepic/pic2.jpg', '7824516272', '256362738142561', 'idproof/adaar1_8OYsFtd.jpg', '76352617283748', '231425', 'Kerala', 'Kottayam', 'Meenachil', 'raju@gmail.com', 3, 'Deactive'),
(3, 'Kiran', 'Home foods', 'signal villas', 'kottyam', 'coverphoto/Tulips.jpg', 'profilepic/pic4.jpg', '9852436152', '5243615243652', 'idproof/Jellyfish.jpg', '635452637653', '324152', 'Kerala', 'Ernakulam', 'Paravur', 'kiran@gmail.com', 5, 'Deactive'),
(4, 'Arya', 'Angadi', 'Hindusthan prv ltd', 'kottayam', 'coverphoto/Desert.jpg', 'profilepic/pic2_vwJZNWq.jpg', '8763547356', '5243615243765', 'idproof/adaar1_IAetB8Q.jpg', '635452637986', '686001', 'Kerala', 'Kottayam', 'Kottayam', 'arya@gmail.com', 7, 'Deactive'),
(5, 'Moncy', 'One&Only Ltd', 'Star Jn', 'kottayam', 'coverphoto/Penguins.jpg', 'profilepic/nandhu.jpg', '7658493029', '465748374657', 'idproof/adaar1_vECVQRx.jpg', '675435647897', '686016', 'Kerala', 'Kottayam', 'Kottayam', 'moncy@gmail.com', 8, 'Deactive'),
(7, 'Jon', 'Kerala Foods', 'lmr villas', 'ktp junction, Ernakulam', 'coverphoto/Jellyfish.jpg', 'profilepic/Tom-Cruise.jpg', '1243516253', '353617283625', 'idproof/adaar1_ol0LL7e.jpg', '536273425162', '686016', 'Kerala', 'Ernakulam', 'Kochi', 'jon@gmail.com', 10, 'Deactive'),
(8, 'Nikhil', 'Nilgris', 'tmt area', 'Kottayam', 'coverphoto/Desert_lEJ8ssu.jpg', 'profilepic/mohanlal.jpg', '9827365243', '635472635172', 'idproof/shop_pic2.jpg', '24256736577', '686008', 'Kerala', 'Kottayam', 'Vaikom', 'nikhil@gmail.com', 11, 'Deactive');

-- --------------------------------------------------------

--
-- Table structure for table `homeapp_user_reg`
--

CREATE TABLE `homeapp_user_reg` (
  `u_id` int(11) NOT NULL,
  `u_name` varchar(200) NOT NULL,
  `u_address` varchar(200) NOT NULL,
  `u_phone` varchar(11) NOT NULL,
  `u_pincode` varchar(6) NOT NULL,
  `user_id_id` int(11) DEFAULT NULL,
  `u_email` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `homeapp_user_reg`
--

INSERT INTO `homeapp_user_reg` (`u_id`, `u_name`, `u_address`, `u_phone`, `u_pincode`, `user_id_id`, `u_email`) VALUES
(1, 'abhi mon', 'kumaranalloor', '9873624152', '735262', 1, NULL),
(2, 'admin', 'admin area', '7000000007', '777777', 4, NULL),
(3, 'rithin', 'hrt bavan', '7652415267', '213241', 6, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `productsapp_product`
--

CREATE TABLE `productsapp_product` (
  `pro_id` int(11) NOT NULL,
  `pro_category` varchar(100) NOT NULL,
  `pro_name` varchar(200) NOT NULL,
  `pro_details` varchar(200) NOT NULL,
  `pro_price` int(11) NOT NULL,
  `pro_rating` int(11) DEFAULT NULL,
  `pro_quantity` int(11) NOT NULL,
  `pro_image` varchar(100) NOT NULL,
  `cat_id_id` int(11) NOT NULL,
  `seller_id_id` int(11) NOT NULL,
  `seller_email` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `productsapp_product`
--

INSERT INTO `productsapp_product` (`pro_id`, `pro_category`, `pro_name`, `pro_details`, `pro_price`, `pro_rating`, `pro_quantity`, `pro_image`, `cat_id_id`, `seller_id_id`, `seller_email`) VALUES
(8, 'Vegitable', 'Carrot New ', 'kerala Fresh', 50, 1, 500, 'Productimages/carrot-regular-500-g-pack-0-20200628.jpg', 1, 3, 'kiran@gmail.com'),
(9, 'Vegitable', 'coconut', 'kerala Kera Product', 58, 1, 1000, 'Productimages/coconut-1-pc-0-20200628.jpg', 1, 3, 'kiran@gmail.com'),
(10, 'Vegitable', 'Onion', 'kerala Product', 89, 1, 100, 'Productimages/onion-1-kg-pack-0-20200628.jpg', 1, 3, 'kiran@gmail.com'),
(18, 'Vegitable', 'Ginger', 'Very Spycy', 30, 1, 50, 'Productimages/ginger-indian-200-g-0-20200628.jpg', 1, 3, 'kiran@gmail.com'),
(19, 'Vegitable', 'Garlic', 'Nice', 22, 1, 40, 'Productimages/garlic-indian-200-g-0-20200628.jpg', 1, 3, 'kiran@gmail.com'),
(20, 'Vegitable', 'Lemon', 'good', 23, 1, 56, 'Productimages/lemon-100-gm-0-20200628.jpg', 1, 3, 'kiran@gmail.com'),
(21, 'Vegitable', 'Chily', 'good', 34, 1, 20, 'Productimages/green-chillies-200-g-0-20200628.jpg', 1, 3, 'kiran@gmail.com'),
(22, 'Stationary', 'Aashirvad Aatta', 'Powder Product', 50, 1, 300, 'Productimages/aashirvaad-select-sharbati-whole-wheat-atta-5-kg-0-20200621.jpeg', 3, 3, 'kiran@gmail.com'),
(24, 'Dairy & Bakery', 'Amul cookie', 'Biscuit', 50, 1, 70, 'Productimages/amul-cooking-butter-100gm-cbd-0-20200518.jpg', 1, 3, 'kiran@gmail.com'),
(25, 'Dairy & Bakery', 'Bread', 'Sweet and Soft', 30, 1, 79, 'Productimages/modern-family-special-bread-400-gm-0-20200522.png', 5, 3, 'kiran@gmail.com'),
(26, 'Snaks & Branded Foods', 'BornVitta New', 'Strenthy mode', 140, 1, 30, 'Productimages/bournvita-750-g-0-20200916.jpg', 6, 3, 'kiran@gmail.com'),
(27, 'Stationary', 'Dove Shine', 'shine product', 30, 1, 120, 'Productimages/dove-daily-shine-shampoo-650-ml-0-20200828.jpg', 3, 3, 'kiran@gmail.com'),
(28, 'Dairy & Bakery', 'Britaniya Good Day', 'Bicute', 40, 1, 60, 'Productimages/britannia-good-day-cashew-cookies-600-g-0-20200621.jpeg', 1, 3, 'kiran@gmail.com'),
(35, 'Vegitable', 'Beetroot', 'Fresh', 24, 1, 60, 'Productimages/None', 1, 8, 'nikhil@gmail.com'),
(37, 'Fruits', 'Mosambi', 'good', 70, 1, 56, 'Productimages/None_sVPZznh', 2, 8, 'nikhil@gmail.com'),
(38, 'Fruits', 'Banana', 'kerala pro', 36, 1, 50, 'Productimages/{self.pk}', 2, 8, 'nikhil@gmail.com'),
(39, 'Fruits', 'Orange', 'good', 56, 1, 90, 'Productimages/None_MGHIxR0', 2, 8, 'nikhil@gmail.com'),
(41, 'Fruits', 'Kiwi', 'good', 56, 1, 90, 'None/kiwi-1-pc-0-20200628.jpg', 2, 8, 'nikhil@gmail.com'),
(42, 'Fruits', 'Pappaya', 'fresh', 50, 1, 70, 'None/papaya-normal-1-5-kg-0-20200628.jpg', 2, 8, 'nikhil@gmail.com'),
(43, 'Fruits', 'Pappaya', 'fresh', 50, 1, 70, 'None/papaya-normal-1-5-kg-0-20200628.jpg Productimages', 2, 8, 'nikhil@gmail.com'),
(44, 'Fruits', 'Pappaya', 'fresh', 50, 1, 70, 'None/papaya-normal-1-5-kg-0-20200628.jpgProductimages', 2, 8, 'nikhil@gmail.com'),
(45, 'Fruits', 'Pappaya', 'fresh', 50, 1, 70, 'None/Productimages/papaya-normal-1-5-kg-0-20200628.jpg', 2, 8, 'nikhil@gmail.com'),
(46, 'Fruits', 'Pappaya', 'fresh', 50, 1, 70, 'None/Productimages/hightlight_final.mp4_snapshot_00.21_2019.12.29_22.20.05.jpg', 2, 8, 'nikhil@gmail.com'),
(47, 'Fruits', 'Pappaya', 'fresh', 50, 1, 70, 'None/ginger-indian-200-g-0-20200628.jpgProductimages', 2, 8, 'nikhil@gmail.com'),
(48, 'Fruits', 'Pappaya', 'fresh', 50, 1, 70, 'None/lemon-100-gm-0-20200628.jpg', 2, 8, 'nikhil@gmail.com'),
(49, 'Fruits', 'Pappaya', 'fresh', 50, 1, 70, 'None/garlic-indian-200-g-0-20200628.jpg', 2, 8, 'nikhil@gmail.com'),
(50, 'Fruits', 'Pappaya', 'fresh', 50, 1, 70, 'None/Productimages/garlic-indian-200-g-0-20200628.jpg', 2, 8, 'nikhil@gmail.com'),
(51, 'Fruits', 'Pappaya', 'fresh', 50, 1, 70, 'None/Productimages/tomato-1-kg-0-20200628.jpg', 2, 8, 'nikhil@gmail.com'),
(52, 'Fruits', 'Pappaya', 'fresh', 50, 1, 70, 'None/Productimages/coconut-1-pc-0-20200628.jpg', 2, 8, 'nikhil@gmail.com'),
(53, 'Vegitable', 'ash', 'good', 78, 1, 45, 'None/Productimages/ash-gourd-slice-500-g-0-20200723.jpg', 1, 8, 'nikhil@gmail.com'),
(54, 'Vegitable', 'ash', 'good', 78, 1, 45, 'Productimages/None_carrot-regular-500-g-pack-0-20200628.jpg', 1, 8, 'nikhil@gmail.com'),
(55, 'Vegitable', 'ash', 'good', 78, 1, 45, 'product/1/sweet-corn-1-pc-0-20200628.jpg', 1, 8, 'nikhil@gmail.com'),
(56, 'Vegitable', 'ash', 'good', 78, 1, 45, 'product/1/tapioca-per-kg-0-20200828.jpg', 1, 8, 'nikhil@gmail.com'),
(58, 'Stationary', 'Bread', 'good pro', 25, 1, 60, 'Productimages/None_modern-enriched-sweet-bread-400-gm-0-20200522.png', 3, 8, 'nikhil@gmail.com'),
(59, 'Dairy & Bakery', 'Amul', 'good', 34, 1, 78, 'Productimages/product_product_object_None_amul-cheese-chiplets-200-g-carton-0-20200909.jpg', 5, 8, 'nikhil@gmail.com'),
(60, 'Dairy & Bakery', 'Amul', 'good', 34, 1, 78, 'Productimages/product_product_object_None_amul-cheese-chiplets-200-g-carton-0-20200909_F9iUYiY.jpg', 5, 8, 'nikhil@gmail.com'),
(61, 'Stationary', 'Milma', 'milk', 26, 1, 40, 'Productimages/django.db.models.query_utils.DeferredAttribute_object_at_0x0000000003FFDB4_Ij0Nqj6.jpg', 3, 8, 'nikhil@gmail.com'),
(62, 'Stationary', 'Milma', 'milk', 26, 1, 40, 'Productimages/django.db.models.query_utils.DeferredAttribute_object_at_0x000000000409DD0_N9GJRPB.jpg', 3, 8, 'nikhil@gmail.com'),
(63, 'Stationary', 'Milma', 'milk', 26, 1, 40, 'Productimages/None_milma-cow-ghee-100-ml-0-20200518.jpg', 3, 8, 'nikhil@gmail.com'),
(64, 'Vegitable', 'Britaniya', 'health', 56, 1, 13, 'productproduct_object_Nonebritannia-cheese-slices-200-g-pack-0-20201007.jpg', 1, 8, 'nikhil@gmail.com'),
(65, 'Vegitable', 'Britaniya', 'health', 56, 1, 13, 'productproduct_object_Nonebritannia-cheese-slices-200-g-pack-0-20201007_H57WXME.jpg', 1, 8, 'nikhil@gmail.com'),
(66, 'Vegitable', 'Britaniya', 'health', 56, 1, 13, 'files/instance_id_None/amulya-dairy-whitener-27-g-pouch-0-20200628.jpg', 1, 8, 'nikhil@gmail.com'),
(67, 'Vegitable', 'Britaniya', 'health', 56, 1, 13, 'Productimages/instance_id_None/hershey-s-chocolate-milkshake-200-ml-tetra-pak-0-20200908.jpg', 1, 8, 'nikhil@gmail.com'),
(68, 'Vegitable', 'Britaniya', 'health', 56, 1, 13, 'Productimages/instance_id_None/hershey-s-chocolate-milkshake-200-ml-tetra-pak-0-20200908_Tj7qJnP.jpg', 1, 8, 'nikhil@gmail.com'),
(69, 'Fruits', 'Apple', 'fresh', 170, 1, 45, 'Productimages/instance_id_None/apple-shimla-value-pack-0-20200828.jpg', 2, 3, 'kiran@gmail.com'),
(70, 'Fruits', 'Apple', 'fresh', 170, 1, 45, 'Productimages_DQS7hEp', 2, 3, 'kiran@gmail.com'),
(71, 'Fruits', 'Apple', 'fresh', 170, 1, 45, 'Productimages_DWC4gNk', 2, 3, 'kiran@gmail.com'),
(72, 'Fruits', 'Apple', 'fresh', 170, 1, 45, 'Productimages_z8dRY65', 2, 3, 'kiran@gmail.com'),
(73, 'Fruits', 'Apple', 'fresh', 170, 1, 45, 'Productimages/seller_reg_s_idNone/pomegranate-kesar-1-kg-0-20200628.jpg', 2, 3, 'kiran@gmail.com'),
(74, 'Fruits', 'Banana New', 'good', 34, 1, 75, 'Productimages/None_EXpRCDw', 2, 8, 'nikhil@gmail.com'),
(75, 'Fruits', 'Banana New', 'good', 34, 1, 75, 'Productimages/None_0NWV4kx', 2, 8, 'nikhil@gmail.com'),
(76, 'Fruits', 'Banana New', 'good', 34, 1, 75, 'Productimages/None_oH1jWvf', 2, 8, 'nikhil@gmail.com'),
(77, 'Fruits', 'Banana New', 'good', 34, 1, 75, 'Productimages/None_SUCovAY', 2, 8, 'nikhil@gmail.com'),
(78, 'Fruits', 'Banana New', 'good', 34, 1, 75, 'Productimages/Nonebanana-njalipoovan-1-kg-0-20200628.png', 2, 8, 'nikhil@gmail.com'),
(79, 'Fruits', 'Banana New', 'good', 34, 1, 75, 'Productimages/None_TnWFuFZ', 2, 8, 'nikhil@gmail.com'),
(80, 'Fruits', 'Banana New', 'good', 34, 1, 75, 'Productimages/Nonebanana-nendran-1-kg-0-20200628.jpg', 2, 8, 'nikhil@gmail.com'),
(81, 'Fruits', 'Banana New', 'good', 34, 1, 75, 'Productimages/Nonebanana-nendran-1-kg-0-20200628_1qhcyWS.jpg', 2, 8, 'nikhil@gmail.com'),
(82, 'Fruits', 'Banana New', 'good', 34, 1, 75, 'Productimages/%s/sNonepapaya-normal-1-5-kg-0-20200628.jpg', 2, 8, 'nikhil@gmail.com'),
(83, 'Fruits', 'Banana New', 'good', 34, 1, 75, 'Productimages/papaya-normal-1-5-kg-0-20200628.jpgNone', 2, 8, 'nikhil@gmail.com'),
(84, 'Fruits', 'Banana New', 'good', 34, 1, 75, 'Productimages/papaya-normal-1-5-kg-0-20200628_S2iboIk.jpgNone', 2, 8, 'nikhil@gmail.com'),
(85, 'Fruits', 'Banana New', 'good', 34, 1, 75, 'Productimages/papaya-normal-1-5-kg-0-20200628_1X47OZj.jpgNone', 2, 8, 'nikhil@gmail.com'),
(86, 'Fruits', 'Banana New', 'good', 34, 1, 75, 'Productimages/filenameNone', 2, 8, 'nikhil@gmail.com'),
(87, 'Fruits', 'Banana New', 'good', 34, 1, 75, 'Productimages/None%s/spapaya-normal-1-5-kg-0-20200628.jpg', 2, 8, 'nikhil@gmail.com'),
(88, 'Fruits', 'Banana New', 'good', 34, 1, 75, 'Productimages/None%s/abcpapaya-normal-1-5-kg-0-20200628.jpg', 2, 8, 'nikhil@gmail.com'),
(89, 'Fruits', 'Banana New', 'good', 34, 1, 75, 'Productimages/None%s/papaya-normal-1-5-kg-0-20200628.jpg', 2, 8, 'nikhil@gmail.com'),
(90, 'Vegitable', 'Apple', 'GOOD', 56, 1, 13, 'Productimages/NonesSapple-shimla-value-pack-0-20200828.jpg', 1, 8, 'nikhil@gmail.com'),
(91, 'Vegitable', 'Apple', 'GOOD', 56, 1, 13, 'Productimages/NonesSapple-shimla-value-pack-0-20200828_sgNyj8p.jpg', 1, 8, 'nikhil@gmail.com'),
(92, 'Vegitable', 'Apple', 'GOOD', 56, 1, 13, 'Productimages/NonesSapple-shimla-value-pack-0-20200828_jb98Sth.jpg', 1, 8, 'nikhil@gmail.com'),
(93, 'Vegitable', 'Apple', 'GOOD', 56, 1, 13, 'Productimages/None%s/apple-shimla-value-pack-0-20200828.jpg', 1, 8, 'nikhil@gmail.com'),
(94, 'Fruits', 'Mathala Naranga', 'god', 160, 1, 39, 'Productimages/pomegranate-kesar-1-kg-0-20200628.jpg', 2, 8, 'nikhil@gmail.com'),
(95, 'Vegitable', 'Pottatto', 'good', 25, 1, 50, 'Productimages/20210707_201537.png', 1, 3, 'kiran@gmail.com'),
(96, 'Vegitable', 'Pottato', 'healthy', 35, 1, 20, 'Productimages/20210707_201537_XFcSS2l.png', 1, 7, 'jon@gmail.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin_sellerapp_add_category`
--
ALTER TABLE `admin_sellerapp_add_category`
  ADD PRIMARY KEY (`cat_id`);

--
-- Indexes for table `admin_sellerapp_approval`
--
ALTER TABLE `admin_sellerapp_approval`
  ADD PRIMARY KEY (`approval_id`),
  ADD KEY `admin_sellerapp_approval_seller_id_id_5c54013c_fk_auth_user_id` (`seller_id_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `homeapp_seller_reg`
--
ALTER TABLE `homeapp_seller_reg`
  ADD PRIMARY KEY (`s_id`),
  ADD KEY `homeapp_seller_reg_seller_id_id_1052ab28_fk_auth_user_id` (`seller_id_id`);

--
-- Indexes for table `homeapp_user_reg`
--
ALTER TABLE `homeapp_user_reg`
  ADD PRIMARY KEY (`u_id`),
  ADD KEY `homeapp_user_reg_user_id_id_3db26031_fk_auth_user_id` (`user_id_id`);

--
-- Indexes for table `productsapp_product`
--
ALTER TABLE `productsapp_product`
  ADD PRIMARY KEY (`pro_id`),
  ADD KEY `productsapp_product_cat_id_id_0a6f7a26_fk_admin_sel` (`cat_id_id`),
  ADD KEY `productsapp_product_seller_id_id_9639a5b9_fk_homeapp_s` (`seller_id_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin_sellerapp_add_category`
--
ALTER TABLE `admin_sellerapp_add_category`
  MODIFY `cat_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `admin_sellerapp_approval`
--
ALTER TABLE `admin_sellerapp_approval`
  MODIFY `approval_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- AUTO_INCREMENT for table `homeapp_seller_reg`
--
ALTER TABLE `homeapp_seller_reg`
  MODIFY `s_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `homeapp_user_reg`
--
ALTER TABLE `homeapp_user_reg`
  MODIFY `u_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `productsapp_product`
--
ALTER TABLE `productsapp_product`
  MODIFY `pro_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=97;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `admin_sellerapp_approval`
--
ALTER TABLE `admin_sellerapp_approval`
  ADD CONSTRAINT `admin_sellerapp_approval_seller_id_id_5c54013c_fk_auth_user_id` FOREIGN KEY (`seller_id_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `homeapp_seller_reg`
--
ALTER TABLE `homeapp_seller_reg`
  ADD CONSTRAINT `homeapp_seller_reg_seller_id_id_1052ab28_fk_auth_user_id` FOREIGN KEY (`seller_id_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `homeapp_user_reg`
--
ALTER TABLE `homeapp_user_reg`
  ADD CONSTRAINT `homeapp_user_reg_user_id_id_3db26031_fk_auth_user_id` FOREIGN KEY (`user_id_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `productsapp_product`
--
ALTER TABLE `productsapp_product`
  ADD CONSTRAINT `productsapp_product_cat_id_id_0a6f7a26_fk_admin_sel` FOREIGN KEY (`cat_id_id`) REFERENCES `admin_sellerapp_add_category` (`cat_id`),
  ADD CONSTRAINT `productsapp_product_seller_id_id_9639a5b9_fk_homeapp_s` FOREIGN KEY (`seller_id_id`) REFERENCES `homeapp_seller_reg` (`s_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
