using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using SQLite;

namespace WpfApp3.Objects
{
    public class Customer
    {
        [PrimaryKey, AutoIncrement] public int Id { get; set; }

        /// <summary> 
        /// 名前 
        /// </summary> 
        public string Name { get; set; }

        /// <summary> 
        /// 電話番号         /// </summary> 
        public string Phone { get; set; }

    }
}
