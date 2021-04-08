//
//  ViewController.swift
//  boredbutton
//
//  Created by Aaron Ruban on 4/6/21.
//
//

import UIKit


class ViewController: UIViewController {
    
    
    @IBOutlet weak var boredButton: UIButton!
    @IBOutlet weak var backRound: UIImageView!
    @IBAction func buttonPressed(_ sender: UIButton) {
        let theColor = colorManager.colors.randomElement()
        print(theColor!)
        let myColor = getColor(theColor!)
        print(myColor ?? "white")
        backRound.backgroundColor = myColor
        }
        
    
    var colorManager = Color()
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        boredButton.layer.cornerRadius = 60
        boredButton.backgroundColor = UIColor.blue
        
    }
    
    func getColor(_ name: String) -> UIColor? {
        let selector = Selector("\(name)Color")
        if UIColor.self.responds(to: selector) {
            let color = UIColor.self.perform(selector).takeUnretainedValue()
            return (color as! UIColor)
        } else {
            return nil
        }
    }
    
    
    
    
}




