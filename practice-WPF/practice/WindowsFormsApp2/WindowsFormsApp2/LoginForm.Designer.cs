
namespace WindowsFormsApp2
{
    partial class LoginForm
    {
        /// <summary>
        /// 必要なデザイナー変数です。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 使用中のリソースをすべてクリーンアップします。
        /// </summary>
        /// <param name="disposing">マネージド リソースを破棄する場合は true を指定し、その他の場合は false を指定します。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows フォーム デザイナーで生成されたコード

        /// <summary>
        /// デザイナー サポートに必要なメソッドです。このメソッドの内容を
        /// コード エディターで変更しないでください。
        /// </summary>
        private void InitializeComponent()
        {
            this.SilverRadioButton = new System.Windows.Forms.RadioButton();
            this.GoldRadioButton = new System.Windows.Forms.RadioButton();
            this.PlatinumRadioButton = new System.Windows.Forms.RadioButton();
            this.ExecutionButton = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // SilverRadioButton
            // 
            this.SilverRadioButton.AutoSize = true;
            this.SilverRadioButton.Checked = true;
            this.SilverRadioButton.Location = new System.Drawing.Point(16, 21);
            this.SilverRadioButton.Name = "SilverRadioButton";
            this.SilverRadioButton.Size = new System.Drawing.Size(63, 16);
            this.SilverRadioButton.TabIndex = 0;
            this.SilverRadioButton.TabStop = true;
            this.SilverRadioButton.Text = "シルバー";
            this.SilverRadioButton.UseVisualStyleBackColor = true;
            // 
            // GoldRadioButton
            // 
            this.GoldRadioButton.AutoSize = true;
            this.GoldRadioButton.Location = new System.Drawing.Point(16, 59);
            this.GoldRadioButton.Name = "GoldRadioButton";
            this.GoldRadioButton.Size = new System.Drawing.Size(61, 16);
            this.GoldRadioButton.TabIndex = 1;
            this.GoldRadioButton.Text = "ゴールド";
            this.GoldRadioButton.UseVisualStyleBackColor = true;
            // 
            // PlatinumRadioButton
            // 
            this.PlatinumRadioButton.AutoSize = true;
            this.PlatinumRadioButton.Location = new System.Drawing.Point(16, 93);
            this.PlatinumRadioButton.Name = "PlatinumRadioButton";
            this.PlatinumRadioButton.Size = new System.Drawing.Size(59, 16);
            this.PlatinumRadioButton.TabIndex = 2;
            this.PlatinumRadioButton.Text = "プラチナ";
            this.PlatinumRadioButton.UseVisualStyleBackColor = true;
            // 
            // ExecutionButton
            // 
            this.ExecutionButton.Location = new System.Drawing.Point(146, 124);
            this.ExecutionButton.Name = "ExecutionButton";
            this.ExecutionButton.Size = new System.Drawing.Size(75, 23);
            this.ExecutionButton.TabIndex = 4;
            this.ExecutionButton.Text = "ログイン";
            this.ExecutionButton.UseVisualStyleBackColor = true;
            this.ExecutionButton.Click += new System.EventHandler(this.ExecutionButton_Click);
            // 
            // LoginForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(284, 261);
            this.Controls.Add(this.ExecutionButton);
            this.Controls.Add(this.PlatinumRadioButton);
            this.Controls.Add(this.GoldRadioButton);
            this.Controls.Add(this.SilverRadioButton);
            this.Name = "LoginForm";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.RadioButton SilverRadioButton;
        private System.Windows.Forms.RadioButton GoldRadioButton;
        private System.Windows.Forms.RadioButton PlatinumRadioButton;
        private System.Windows.Forms.Button ExecutionButton;
    }
}

