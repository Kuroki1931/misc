using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static WindowsFormsApp2.MemberFactory;

namespace WindowsFormsApp2
{
    public partial class LoginForm : Form
    {
        public LoginForm()
        {
            InitializeComponent();
        }

        private void ExecutionButton_Click(object sender, EventArgs e)
        {
            MemberKind memberKind = MemberKind.Silver;
            if (SilverRadioButton.Checked){
                memberKind = MemberKind.Silver;
            }
            else if (GoldRadioButton.Checked)
            {
                memberKind = MemberKind.Gold;
            }
            else
            {
                memberKind = MemberKind.Platinum;
            }

            LoginInfo.Member = MemberFactory.Create(memberKind);

            using (var f = new Form1())
            {
                f.ShowDialog();
            }
        }
    }
}
