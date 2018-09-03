CREATE TABLE IF NOT EXISTS `mail_list` (
  `id` bigint(20) unsigned NOT NULL  ,
  `name` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `user` (
  `id` bigint(20)  unsigned NOT NULL  ,
  `mail_id` bigint(200) unsigned NOT NULL ,
  PRIMARY KEY (`id`), 
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- Dumping structure for table beta_homeyantra.addresses
CREATE TABLE IF NOT EXISTS `mail_list_user` (
  `mail_id` bigint(20)  unsigned NOT NULL ,
  `user_id` bigint(20) unsigned  NOT NULL,
  KEY `mail_list_id` (`mail_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `mail_list_id` FOREIGN KEY (`mail_id`) REFERENCES `mail_list` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='All addresses ever!';

-- Dumping structure for table beta_homeyantra.recommended_products
CREATE TABLE IF NOT EXISTS `mail_session` (
  `id` bigint(20)  unsigned NOT NULL ,
  `content` varchar(100000)   NOT NULL,
  `subject` varchar(500) NOT NULL ,
  `date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
 ) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- Data exporting was unselected.

CREATE TABLE IF NOT EXISTS `mail_session_user` (
  `mail_session_id` bigint(20)   NOT NULL ,
  `user_id` varchar(100) NOT NULL,
  `flag` tinyint(20)  unsigned NOT NULL DEFAULT '0',
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='List of attributes available across all products';

-- Data exporting was unselected.
-- Dumping structure for table beta_homeyantra.attribute_category
